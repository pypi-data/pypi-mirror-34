from lantern_flask.utils.json import json_decimal_to_float, json_float_to_decimal

def http_response(code, message, data, count=None, next=None, response=None):
    """ Format a return a valid JSON
    
    Arguments:
        code {int} -- Valid HTTP Status Code
        message {str} -- Message to be sent
        data {json} -- Json to be returned
    
    Keyword Arguments:
        count {int} -- count if we return multiple values (default: {None})
        next {json} -- current search index, for pagination (default: {None})
        response {res} -- a valid http response (default: {None})
    
    Returns:
        [type] -- [description]
    """
    data = json_decimal_to_float(data)
    data_json = {
        "status": code,
        "message": message,
        "results": data,
    }
    if count:
        data_json["count"] = count
    if next:
        data_json["next"] = next
    if response:
        data_json["raw"] = response
    return data_json


def http_error(code, message, detail, e=None):
    """ return a standard json response for errors """
    data = {
        "status": code,
        "message": message,
        "detail": detail,
    }
    if e:
        data["raw"] = str(e)
    return data