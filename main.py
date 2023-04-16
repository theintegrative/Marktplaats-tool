import requests
import json

def advertisements():
    url = 'https://www.marktplaats.nl/lrp/api/search'

    querystring = {
        'attributesById[]': 10898,
        'attributesById[]': 10882,
        'l1CategoryId': 1953,
        'limit': 30,
        'offset': 2
        }

    headers = {
        }

    response = requests.get(url, headers=headers, params=querystring)
    json_object = json.loads(response.content)
    json_formatted_str = json.dumps(json_object, indent=1)
    print(json_formatted_str)



    
advertisements()
