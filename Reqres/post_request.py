import json

import requests

base_url = "https://reqres.in"


# POST Request
def create_user():
    url = base_url + "/api/user"
    post_data = {
        "name": "morpheus",
        "job": "leader"
    }

    response = requests.post(url, data=post_data)
    json_body = response.json()
    json_body_formatted = json.dumps(json_body, indent=4)
    print(f"json_body_formatted : {json_body_formatted}")
    assert response.status_code == 201, f"Unable to create user"
    print(f"Status code : {response.status_code}")
    uid = json_body['id']
    print(f"USER ID : {uid}")
    return uid


user_id = create_user()


def get_user(status_code, uid):
    url = base_url + f"/api/users/{uid}"
    response = requests.get(url)
    json_body = response.json()
    json_body_formatted = json.dumps(json_body, indent=4)
    print(f"json_body_formatted : \n{json_body_formatted}")
    print(f"Status code : {response.status_code}")
    assert response.status_code == status_code


# get_user(200, user_id)


# PUT Request
def update_user_using_put(uid):
    url = base_url + f"/api/user/{uid}"
    post_data = {
        "name": "morpheus",
        "job": "zion resident"
    }

    response = requests.patch(url, data=post_data)
    json_body = response.json()
    json_body_formatted = json.dumps(json_body, indent=4)
    print(f"json_body_formatted : {json_body_formatted}")
    assert response.status_code == 200, f"Unable to update user data"
    print(f"Status code : {response.status_code}")


update_user_using_put(user_id)


# PATCH Request
def update_user_using_patch(uid):
    url = base_url + f"/api/user/{uid}"
    post_data = {
        "name": "morpheus",
        "job": "zion resident",
        "email": "morpheus@yahoo.com"
    }

    response = requests.patch(url, data=post_data)
    json_body = response.json()
    json_body_formatted = json.dumps(json_body, indent=4)
    print(f"json_body_formatted : {json_body_formatted}")
    assert response.status_code == 200, f"Unable to update user data"
    print(f"Status code : {response.status_code}")


update_user_using_patch(user_id)


def delete_user(uid):
    url = base_url + f"/api/user/{uid}"
    response = requests.delete(url)
    print(f"Status code : {response.status_code}")
    assert response.status_code == 204


delete_user(user_id)
