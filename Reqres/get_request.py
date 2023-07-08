import json

import requests


base_url = "https://reqres.in"


def get_request_list_user():
    url = base_url + "/api/users?page=2"
    response = requests.get(url)
    json_body = response.json()
    json_body_formatted = json.dumps(json_body, indent=4)
    print(f"json_body_formatted : \n{json_body_formatted}")
    assert response.status_code == 200
    print(f"Status code : {response.status_code}")


# get_request_list_user()


def get_request_single_user(status_code):
    url = base_url + "/api/users/2"
    response = requests.get(url)
    json_body = response.json()
    json_body_formatted = json.dumps(json_body, indent=4)
    print(f"json_body_formatted : \n{json_body_formatted}")
    assert response.status_code == status_code
    print(f"Status code : {response.status_code}")


# get_request_single_user(200)


def get_request_single_user_not_found(status_code):
    url = base_url + "/api/users/23"
    response = requests.get(url)
    json_body = response.json()
    json_body_formatted = json.dumps(json_body, indent=4)
    print(f"json_body_formatted : \n{json_body_formatted}")
    assert response.status_code == status_code
    print(f"Status code : {response.status_code}")


# get_request_single_user_not_found(404)

def get_request_list_resource():
    url = base_url + "/api/unknown"
    response = requests.get(url)
    json_body = response.json()
    json_body_formatted = json.dumps(json_body, indent=4)
    print(f"json_body_formatted : \n{json_body_formatted}")
    assert response.status_code == 200
    print(f"Status code : {response.status_code}")


# get_request_list_resource()


def get_request_single_resource(status_code):
    url = base_url + "/api/unknown/2"
    response = requests.get(url)
    json_body = response.json()
    json_body_formatted = json.dumps(json_body, indent=4)
    print(f"json_body_formatted : \n{json_body_formatted}")
    assert response.status_code == status_code
    print(f"Status code : {response.status_code}")


# get_request_single_resource(200)


def get_request_single_resource_not_found(status_code):
    url = base_url + "/api/unknown/23"
    response = requests.get(url)
    json_body = response.json()
    json_body_formatted = json.dumps(json_body, indent=4)
    print(f"json_body_formatted : \n{json_body_formatted}")
    assert response.status_code == status_code
    print(f"Status code : {response.status_code}")


get_request_single_resource_not_found(404)

