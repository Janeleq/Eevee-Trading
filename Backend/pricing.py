# Pricing Microservice to show different CC prices on simulator page
# Activated upon entering simulator -> /simulator
import requests

# invoke Crytocompare API to get different pricing according to specific CC
response = requests.get("http://randomfox.ca/floof")
print(response.status_code, response.json())