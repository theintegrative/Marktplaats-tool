import requests
import json
from pprint import pprint

## Variables
# Api documentation https://api.marktplaats.nl/docs/v1/search-advertisements.html
def search_query(query, offset, limit, catagory=820):
    query = {
        'query': query, 
        'offset': offset,
        'limit': limit,
        'l1CategoryId': catagory
        }
    return query

def advertisements(querystring):
    url = 'https://www.marktplaats.nl/lrp/api/search'
    response = requests.get(url, headers={}, params=querystring)
    json_object = json.loads(response.content)
    return json.dumps(json_object, indent=4)

querystring = search_query("iphone", 30, 2)
pprint(advertisements(querystring))
