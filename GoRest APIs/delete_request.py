import json

import requests

base_url = "https://gorest.co.in"
auth_token = "Bearer 2e083ce35ec2d4e6f1298eedc998dfb43560ea8b89bc8360480c046febf1927d"


def get_request():
    url = base_url + "/public/v2/users"
    print(f"GET URL : {url}")
    header = {"Authorization": auth_token}
    response = requests.get(url, headers=header)
    json_body = response.json()
    print(f"Response body : {json_body}")
    json_body_formatted = json.dumps(json_body, indent=4)
    print(f"Response body formatted : {json_body_formatted}")
    assert response.status_code == 200
    uid = json_body[0]['id']
    return uid


def get_request_single_user(uid, status_code):
    url = base_url + f"/public/v2/users/{uid}"
    print(f"GET URL (for single user): {url}")
    header = {"Authorization": auth_token}
    response = requests.get(url, headers=header)
    json_body = response.json()
    print(f"Response body : {json_body}")
    json_body_formatted = json.dumps(json_body, indent=4)
    print(f"Response body formatted : {json_body_formatted}")
    assert response.status_code == status_code


def delete_request(uid):
    url = base_url + f"/public/v2/users/{uid}"
    print(f"DELETE URL : {url}")
    header = {"Authorization": auth_token}
    response = requests.delete(url, headers=header)
    assert response.status_code == 204
    print("******* DELETE DONE *******")


user_id = get_request()
get_request_single_user(user_id, 200)
delete_request(user_id)
get_request_single_user(user_id, 404)





