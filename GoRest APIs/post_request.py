import requests
import random
import json
import string

base_url = "https://gorest.co.in"

auth_token = "Bearer 2e083ce35ec2d4e6f1298eedc998dfb43560ea8b89bc8360480c046febf1927d"


def post_request():
    url = base_url + "/public/v2/posts"
    print("POST Request URL : ", url)
    headers = {"Authorization": auth_token}
    post_body = {
                    "name": "Tanu Sharma",
                    "email": "tanu_sharma@dicki.test",
                    "gender": "female",
                    "status": "active"
                }

    response = requests.post(url, data=post_body, headers=headers)
    json_data = response.json()
    actual_json_data = json.dumps(json_data, indent=4)
    print("JSON POST body (json_data): ", json_data)
    print("JSON POST body (actual_json_data): ", actual_json_data)
    print("Request status code : ", response.status_code)
    assert response.status_code == 201



post_request()


