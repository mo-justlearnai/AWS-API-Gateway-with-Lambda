# ==================================================
# Title: API Call testing
# Author: Mattithyahu
# Created Date: 29/08/2023
# ==================================================
# To rest: RUN `python client.py`

# Imports
# ==================================================
import json
import requests


# API Call 
# ==================================================
url = 'https://r19a9qff84.execute-api.eu-west-2.amazonaws.com/prod/'

headers = {'Accept': 'application/json', 
           'x-api-key': 'O10E94jiHk8e9wjS5V8vj7IPVALp8BgAa7FcR0w3'
          }

dicts = {
    'name': 'Mattithyahu'
}

request_data = json.dumps(dicts)


# POST METHOD 
# ==================================================
response = requests.post(url, request_data, headers=headers)

try:
    print("Status Code: " + str(response.status_code))
    print("Message: " + (response.json()['body']))

except Exception as e:
    print(f"Errors : {e} ")
    print("Status Code: " + str(response.status_code))
    print(response.text)