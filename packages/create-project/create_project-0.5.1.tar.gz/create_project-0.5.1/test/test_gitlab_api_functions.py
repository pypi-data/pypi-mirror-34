# -----------------------------------------------------------------------------
# Created: Sun 15 Jul 2018 18:36:10 IST
# Last-Updated: Sun 12 Aug 2018 18:18:47 IST
#
# test_gitlab_api_functions.py is part of create-project
# URL: https://gitlab.com/justinethomas/create-project
# Description: Main test file.
#
# Copyright (c) 2018, Justine T Kizhakkinedath
# All rights reserved
#
# Licensed under the terms of MIT License
# See LICENSE file in the project root for full information.
# -----------------------------------------------------------------------------
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
# OR OTHER DEALINGS IN THE SOFTWARE.
#
# -----------------------------------------------------------------------------

from create_project import gitlab_api, secret


# # Works
# def test_get_list_of_projects():
#     assert(gitlab_api.get_list_of_projects().status_code) == 200


# # Works
# def test_create_project():
#     payload_data = {"new_project_name": "Foo Bar",
#                     "project_description": "Random description",
#                     "visibility_level": "public"}
#     assert gitlab_api.create_gitlab_project(payload_data
#     ).status_code == 201


# # Works
# def test_create_project_group():
#     payload_data = {"new_project_name": "Foo Bar",
#                     "namespace": secret.group_name,
#                     "project_description": "Random description",
#                     "visibility_level": "public"}
#     assert gitlab_api.create_gitlab_project_group(payload_data
#     ).status_code == 201

# Works
# def test_get_namespace_id():
#     assert(gitlab_api.get_namespace_id("justinekizhak-testing") == 3426320 )

# # Works
# def test_get_project_id():
#     assert gitlab_api.get_project_id("header3") == 6980862
#     assert(gitlab_api.get_project_id("laskdfjl") == None)


# # Works
# def test_get_project_labels():
#     assert gitlab_api.get_project_labels("dotfiles").status_code == 200


# # Works
# def test_create_project_labels():
#     payload_data = {"label_name": "demo", "label_color": "#5843AD"}
#     assert gitlab_api.create_project_labels(
#         "dotfiles", payload_data).status_code == 201


# # Works
# def test_get_project_board():
#     assert gitlab_api.get_project_board(
#         "dotfiles").status_code == 200


# def test_create_project_board():
#     assert gitlab_api.create_project_board(
#         "dotfiles", "Everything").status_code == 201


# # Works
# def test_get_board_id():
#     assert gitlab_api.get_board_id(
#         "dotfiles", "Enhancement") == 666423


# # Works
# def test_rename_board():
#     assert gitlab_api.rename_board(
#         "dotfiles", "Development", "Enhancement").status_code == 200

# # Works
# def test_get_label_id():
#     assert gitlab_api.get_label_id(
#         "dotfiles", "Type: Bug") == 7106890


# # Works
# def test_create_board_list():
#     payload_data = {"board_name": "Enhancement",
#                     "Labels": ["Status: To Do",
#                                "Status: In Progress",
#                                "Status: In Review"]}
#     for label in payload_data["Labels"]:
#         assert gitlab_api.create_board_list(
#             "dotfiles", payload_data["board_name"],
#             label).status_code == 201
