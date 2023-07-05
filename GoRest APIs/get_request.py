import requests
import random
import json
import string

base_url = "https://gorest.co.in"

auth_token = "Bearer 2e083ce35ec2d4e6f1298eedc998dfb43560ea8b89bc8360480c046febf1927d"


def get_request():
    url = base_url + "/public/v2/users"
    print("GET Request URL : ", url)
    headers = {"Authorization": auth_token}
    response = requests.get(url, headers=headers)
    json_data = response.json()
    actual_json_data = json.dumps(json_data, indent=4)
    print("JSON GET response body (json_data) : ", json_data)
    print("JSON GET response body (actual_json_data) : ", actual_json_data)
    assert response.status_code == 200


get_request()

# If you want to run the same scenario from command prompt
# Go to this directory - C:\Users\Vibhor\Documents\GitHub\Python-API\GoRest APIs
# Run command = python get_request.py

