import boto3
import logging
from lantern_flask.utils.json import json_float_to_decimal
from lantern_flask.utils.request import http_response, http_error
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')
log = logging.getLogger(__name__)


class ExceptionInvalidDynamoControllerType(Exception):
    """ Dynamo Type Not defined, this is a programming error """
    pass


class ExceptionInvalidDynamoControllerNotFound(Exception):
    """ Object not found in DB (404 error) """
    pass


class DynamoController(object):
    """ Generic Dynamo Access Controller
        - Error handling
        - response message/data normalization
    """

    TYPE_GET = "get"
    TYPE_CREATE = "create"
    TYPE_UPDATE = "update"
    TYPE_DELETE = "delete"

    ORDER_ASC = "asc"
    ORDER_DESC = "desc"


    def __init__(self, table_name, return_raw_objects=False, filter_by_username=True):
        """ Initialize Dynamo Controller

        Arguments:
            table_name {str} -- Dynamo table name
            return_raw_objects {bool} -- if true, we return the raw object returned from Dynamo, any other case we return a proper http_response obj
            filter_by_username {bool} -- If true, this controller will filter and validate username in session with handled records.
        """
        self.table = dynamodb.Table(table_name)
        self.return_raw_objects = return_raw_objects
        self.filter_by_username = filter_by_username

    def get(self, primary_keys):
        """ return a the first element corresponding to the filter_data param """
        res = self._execute_operation(
            type=self.TYPE_GET, primary_keys=primary_keys)
        return res, res["status"]

    def create(self, data):
        """ Creates a new instance in the DB.
            - Overrides by primary key)
            - Returns the new/updated element
        """
        res = self._execute_operation(type=self.TYPE_CREATE, data=data)
        return res, res["status"]

    def update(self, primary_keys, data):
        """ Update an existing object in the database
            - Returns the updated object
        """
        res = self._execute_operation(
            type=self.TYPE_GET, primary_keys=primary_keys)
        if res["status"] != 200:
            return res
        res = self._execute_operation(
            type=self.TYPE_UPDATE, primary_keys=primary_keys, data=data)
        return res, res["status"]

    def delete(self, primary_keys):
        """ Deletes a set of objects, corresponding to filter_data
            - Delete the specific element
        """
        res = self._execute_operation(
            type=self.TYPE_GET, primary_keys=primary_keys)
        if res["status"] != 200:
            return res
        res = self._execute_operation(
            type=self.TYPE_DELETE, primary_keys=primary_keys)
        return res, res["status"]
    

    def filter(self, key, value, order_by=None, limit=50, next=None, index=None, order_type=ORDER_DESC):
        """ Return all orders related to this user
        """
        if index:
            index_name = index
        elif key and order_by:
            index_name = "{}-{}-index".format(key, order_by)
        else:
            index_name = "{}-index".format(key)

        params = {
            "IndexName": index_name,
            "KeyConditionExpression":Key(key).eq(value),
            "Limit":limit,
        }
        if next:
            params["ExclusiveStartKey"] = next
        
        if order_type == self.ORDER_DESC:
            params["ScanIndexForward"] = False

        response = self.table.query(**params)
        data = response["Items"] if response["Count"] != 0 else []
        count = response["Count"]
        next = response["LastEvaluatedKey"] if "LastEvaluatedKey" in response else None
        code = response['ResponseMetadata']['HTTPStatusCode']
        return http_response(code=code, message="Fetched", data=data, count=count, next=next)

    def _execute_operation(self, type, primary_keys=None, data=None):
        """ Execute the dynamo operation and return a proper response (success or error)
        """
        try:
            if type == self.TYPE_GET:
                d_res = self.table.get_item(Key=primary_keys)
                if "Item" in d_res:
                    data = d_res["Item"]
                else:
                    raise ExceptionInvalidDynamoControllerNotFound("Not Found")
                if self.return_raw_objects:
                    return data
                else:
                    code = d_res['ResponseMetadata']['HTTPStatusCode']
                    return http_response(code=code, message="Fetched", data=data)
            elif type == self.TYPE_CREATE:
                data = json_float_to_decimal(data)
                d_res = self.table.put_item(Item=data)
                if self.return_raw_objects:
                    return data
                else:
                    code = d_res['ResponseMetadata']['HTTPStatusCode']
                    return http_response(code=code, message="Created", data=data)
            elif type == self.TYPE_UPDATE:
                data = json_float_to_decimal(data)
                data.update(primary_keys)
                d_res = self.table.put_item(Item=data)
                if self.return_raw_objects:
                    return data
                else:
                    code = d_res['ResponseMetadata']['HTTPStatusCode']
                    return http_response(code=code, message="Updated", data=data)
            elif type == self.TYPE_DELETE:
                d_res = self.table.delete_item(Key=primary_keys)
                log.info(d_res)
                if self.return_raw_objects:
                    return primary_keys
                else:
                    code = d_res['ResponseMetadata']['HTTPStatusCode']
                    return http_response(code=code, message="Deleted", data=primary_keys)
            else:
                raise ExceptionInvalidDynamoControllerType(
                    "Type {} not defined in DynamoController".format(type))
        except ExceptionInvalidDynamoControllerType as e:
            return http_error(code=500, message="Type not defined in controller", detail=str(e))
        except ExceptionInvalidDynamoControllerNotFound as e:
            return http_error(code=404, message="Element Not Found", detail=str(e))
        except Exception as e:
            return http_error(code=500, message="Unexpected error", detail=str(e))