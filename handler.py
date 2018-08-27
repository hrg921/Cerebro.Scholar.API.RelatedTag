import json
import elastic_search


def main(event, context):
    params = event['queryStringParameters']
    print(params)
    if params["tag"] is not list:
        params["tag"] = [params["tag"]]
    if params.get("sort") is not "co_occur":
        params["sort"] = "relatedwords.genyear"

    result = elastic_search.get(params)

    response = {
        "statusCode": 200,
        "body": json.dumps(result)
    }

    return response


# def get_related_keywords(input_,co_occur=True, size=10, order='desc'):
#     """
#       input_ : 'machine learning', 'internet of things (iot)', 'machine learning+internet of things (iot)'
#                 만 가능, 주의-keyword로 검색해서 spacebar 하나달라도 다른 글자로 인식함
#     """
#     if input_ is not list:
#       input_ = [input_]
#     sort = 'relatedwords.co_occur' if co_occur else 'relatedwords.genyear'
#     params = { 'input' : input_, 'sort' : sort, 'order' : order, 'size' : size}
#
#     return request(params)
