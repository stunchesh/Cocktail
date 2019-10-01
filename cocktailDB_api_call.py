import requests
import json
def jprint(obj):
    #create a formatted strting of the python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print (text)

response = requests.get("https://www.thecocktaildb.com/api/json/v1/1/search.php?f=a")
jprint(response.json())

