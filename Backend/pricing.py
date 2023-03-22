# Pricing Microservice

import requests

# invoke Crytocompare API to get different pricing according to specific CC
response = requests.get("http://randomfox.ca/floof")
print(response.status_code, response.json())