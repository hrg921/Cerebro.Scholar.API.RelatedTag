"""
Created by hangeonho on 2018. 8. 22..
"""


def get(params):
    query = {
        "size": params.get('size', 16),
        "query": {
            "match": {
                "searchword": '+'.join(i for i in params['tag'])
            }
        },
        "_source": "relatedwords",
        "sort": [
            {
                params['sort']: {
                    "order": params.get('order', 'desc'),
                    "nested": {
                        "path": "relatedwords"
                    }
                }
            }
        ]
    }
    return query
