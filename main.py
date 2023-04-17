import requests
import json
from pprint import pprint

# Api documentation https://api.marktplaats.nl/docs/v1/search-advertisements.html
def search_query(query, offset, limit, catagory=820):
    query = {
        'query': query, 
        'offset': offset,
        'limit': limit,
        'l1CategoryId': catagory,
        'viewOptions': "list-view",
        'totalCount': 1000
        }
    return query

def advertisements(querystring):
    url = 'https://www.marktplaats.nl/lrp/api/search'
    response = requests.get(url, headers={}, params=querystring)
    json_object = json.loads(response.content)
    return json.dumps(json_object, indent=4)

## save json result
def save_query(advertisements):
    with open("search.json", "w") as file:
        json.dump(json.loads(advertisements), file, indent=4)

def load_query():
    with open("search.json", "r") as file:
        return json.load(file)

def filter_ads(advertisements):
    processed = []
    for ad in advertisements["listings"]:
        try:
            location = ad["location"]["cityName"]
        except:
            location = None
        processed.append(
                {
                    "url": f"https://www.marktplaats.nl{ad['vipUrl']}",
                    "location": location,
                    "priceInfo": ad["priceInfo"],
                    "date": ad["date"]
                    }
                )
    return processed
        
if __name__ == '__main__':
    # For some reason a limit above 100 does not work
    # querystring = search_query("iphone", 1, 100)
    # ads = advertisements(querystring)
    # save_query(ads)
    pprint(filter_ads(load_query()))
