import json
import elastic_search


def main(event, context):
    params = event['queryStringParameters']
    print(params)
    if type(params["tag"]) is not list:
        params["tag"] = [params["tag"]]
    if params.get("sort") is not "co_occur":
        params["sort"] = "relatedwords.genyear"

    if params.get("version") == 0:
        result = elastic_search.get(params)
    elif params.get("version") == 1:
        params['size'] = params['size'] / 2.0
        result = elastic_search.get_by_graphapi(params)
    elif params.get("version") == 2:
        result = elastic_search.get_by_significant_term(params)

    response = {
        "statusCode": 200,
        "body": json.dumps(result)
    }

    return response