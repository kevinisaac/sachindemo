import requests
import json

response = requests.get('https://cat-fact.herokuapp.com/facts/')

print(response.status_code)
print(json.dumps(response.json(), indent=4))

