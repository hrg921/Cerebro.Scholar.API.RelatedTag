"""
Created by hangeonho on 2018. 8. 22..
"""
import ast

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

def get_by_graphapi(params):
  """
    "tag" : list of keywords
    "date" : papers starting from params['date']
    "min_doc_count" : The minimum frequency of keywords in the entire document.
  """
    query = {
        "query": {
            "bool": {
              "must":
                list(ast.literal_eval(', '.join( [ str({ "match" : { "keywords_tag" :  i  } }) for i in params.get('tag') ] )))
            }
        },
        "controls": {
            "sample_size": 75001,
            "timeout": 5000
        },
        "connections": {
              "query" : {
                "bool": {
                  "filter": [
                   {
                    "range": {
                       "start_date.min_date": {
                          "gte": params.get('date')
                       }
                    }
                   }
                  ]
                 }
              },
                "vertices": [
                    {
                        "field": "keywords_tag",
                        "size": params.get('size', 8),
                        "min_doc_count": params.get('min_doc_count'),
                        "exclude" : params.get('tag')
                    }
                ]
        },
        "vertices": [
            {
                "field": "keywords_tag",
                "size": params.get('size', 8),
                "min_doc_count": params.get('min_doc_count'),
                "exclude" : params.get('tag')
            }
        ]
    }
    return query

def get_by_agg_signicant_terms(params):
    query = {
      "size": 0, 
        "query" : {
          "bool": {
            "must": 
              list(ast.literal_eval(', '.join( [ str({ "match" : { "keywords_tag" :  i  } }) for i in params.get('tag') ] )))
          }
        },
        "aggregations" : {
            "significant_related_word" : {
              "significant_terms" : { 
                "field" : "keywords_tag",
                "exclude": params.get("tag")
              }
            }
        }
    }
    return query