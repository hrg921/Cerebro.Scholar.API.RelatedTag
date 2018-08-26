"""
Created by hangeonho on 2018. 8. 22..
"""
import requests
import json
import query

def get(params):
    return request(params)

def get_by_graphapi(params):
    return request_v1(params)

def get_by_significant_term(params):
    return request_v2(params)

def request(params):
    """
    url : index - related / type : words
    params :  input - query string (keyword)
              sort - key of sort [ genyear : generated year of keyword, co_occur : co-occurance count of related keyword]
    order : order of sort [ 'asc', 'desc' ]
  """
    URL = 'https://fd2b16254da343159c56f09ad393c420.us-west-1.aws.found.io:9243/related/words/_search'
    headers = {'Accept': 'text/plain', 'Content-type': 'application/json'}

    # if params['input'] is not list:
    # params['input'] = [ params['input'] ]

    # sort = 'relatedwords.co_occur' if co_occur else 'relatedwords.genyear'

    r = requests.get(URL, data=json.dumps(query.get(params)), headers=headers, auth=('elastic', 'Ftkn0jSUxwI867OzNmPiAVeu'))
    hits = json.loads(r.text)['hits']['hits']
    if len(hits) > 0:
        return [h['_source']['relatedwords'] for h in hits]
    return []

def request_v1(params):
    URL = 'https://fd2b16254da343159c56f09ad393c420.us-west-1.aws.found.io:9243/papers/doc/_search'
    headers = {'Accept': 'text/plain', 'Content-type': 'application/json'}

    r = requests.get(URL, data=json.dumps(query.get_by_graphapi(params)), headers=headers, auth=('elastic', 'Ftkn0jSUxwI867OzNmPiAVeu'))
    hits = json.loads(r.text)['vertices']
    if len(hits) > 0:
        return [h['term'] for h in hits]
    return []

def request_v2(params):
    URL = 'https://fd2b16254da343159c56f09ad393c420.us-west-1.aws.found.io:9243/papers/doc/_search'
    headers = {'Accept': 'text/plain', 'Content-type': 'application/json'}

    r = requests.get(URL, data=json.dumps(query.get_by_agg_signicant_terms(params)), headers=headers, auth=('elastic', 'Ftkn0jSUxwI867OzNmPiAVeu'))
    hits = json.loads(r.text)['aggregations']['significant_related_word']['buckets']
    if len(hits) > 0:
        return [h['key'] for h in hits]
    return []