#!/usr/bin/env python3
# -----------------------------------------------------------------------------
# Copyright (c) 2018, Justine T Kizhakkinedath
# All rights reserved
#
# Licensed under the terms of MIT License
# See LICENSE file in the project root for full information.
# -----------------------------------------------------------------------------

import requests
from create_project import secret

base_url = "https://gitlab.com/api/v4"


def create_gitlab_project(payload_data):
    payload = {
        "name": payload_data["name"],
        "description": payload_data["description"],
        "visibility": payload_data["visibility"]
    }
    headers = {"PRIVATE-TOKEN": secret.token}
    response = requests.post(base_url + "/projects/",
                             data=payload, headers=headers)
    return response

def get_namespace_id(namespace):
    headers = {"PRIVATE-TOKEN": secret.token}
    response = requests.get(base_url + "/namespaces?search="
                            + namespace,
                            headers=headers)
    data = response.json()
    for user in data:
        if(user["name"] == namespace):
            return user["id"]

def create_gitlab_project_group(payload_data):
    payload = {
        "name": payload_data["new_project_name"],
        "namespace_id": get_namespace_id(payload_data["namespace"]),
        "description": payload_data["project_description"],
        "visibility": payload_data["visibility_level"]
    }
    headers = {"PRIVATE-TOKEN": secret.token}
    response = requests.post(base_url + "/projects/",
                             data=payload, headers=headers)
    return response

def get_list_of_projects():
    headers = {"PRIVATE-TOKEN": secret.token}
    response = requests.get(base_url + "/users/"
                        + secret.user_id
                        + "/projects/",
                        headers=headers)
    return response


def get_project_id(project_name):
    data = get_list_of_projects().json()
    for project in data:
        if(project["name"] == project_name):
            return project["id"]
    return(None)



def get_project_labels(project_name):
    headers = {"PRIVATE-TOKEN": secret.token}
    response = requests.get(base_url + "/projects/"
                        + str(get_project_id(project_name))
                        + "/labels",
                        headers=headers)
    return response


def create_project_labels(project_name, payload_data):
    payload = {
        "name": payload_data["name"],
        "color": payload_data["color"],
        "priority": payload_data["priority"],
    }
    headers = {"PRIVATE-TOKEN": secret.token}
    response = requests.post(base_url + "/projects/"
                         + str(get_project_id(project_name))
                         + "/labels",
                         data=payload,
                         headers=headers)
    return response


def get_project_boards(project_name):
    headers = {"PRIVATE-TOKEN": secret.token}
    response = requests.get(base_url + "/projects/"
                        + str(get_project_id(project_name))
                        + "/boards",
                        headers=headers)
    return(response)


def create_project_board(project_name, board_name):
    payload = {
        "name": board_name,
    }
    headers = {"PRIVATE-TOKEN": secret.token}
    response = requests.post(base_url + "/projects/"
                         + str(get_project_id(project_name))
                         + "/boards",
                         data=payload,
                         headers=headers)
    return response


def get_board_id(project_name, board_name):
    project_boards = get_project_boards(project_name).json()
    for project_board in project_boards:
        if(project_board["name"] == board_name):
            return(project_board["id"])

def rename_board(project_name, board_name_old, board_name_new):
    payload = {
        "name": board_name_new,
    }
    headers = {"PRIVATE-TOKEN": secret.token}
    response = requests.put(base_url + "/projects/"
                        + str(get_project_id(project_name))
                        + "/boards/"
                        + str(get_board_id(project_name, board_name_old)),
                        data=payload,
                        headers=headers)
    return response

def get_label_id(project_name, label_name):
    labels = get_project_labels(project_name).json()
    for label in labels:
        if(label["name"] == label_name):
            return(label["id"])

def create_board_list(project_name, board_name, label_name):
    payload = {
        "label_id": str(get_label_id(project_name, label_name))
    }
    headers = {"PRIVATE-TOKEN": secret.token}
    response = requests.post(base_url + "/projects/"
                         + str(get_project_id(project_name))
                         + "/boards/"
                         + str(get_board_id(project_name, board_name))
                         + "/lists/",
                         data=payload,
                         headers=headers)
    return response
