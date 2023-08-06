# -----------------------------------------------------------------------------
# Created: Sun 22 Jul 2018 22:48:09 IST
# Last-Updated: Sun 12 Aug 2018 16:41:55 IST
#
# test_create_complete_project.py is part of create_project
# URL: https://gitlab.com/justinethomas/create_project
# Description:
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


from create_project import gitlab_api as gl
from create_project import read_yaml as ry


# # Works
# def test_create_complete_project():
#     project_name = ry.get_project_name()

#     assert gl.create_gitlab_project(
#         project_name,
#         ry.get_project_description(),
#         ry.get_project_visibility()
#     ) == 201

#     for label in ry.get_project_labels():
#         assert gl.create_project_labels(
#             project_name,
#             label["name"],
#             label["color"]
#         ) == 201

#     for board in ry.get_project_boards():
#         assert gl.create_project_board(
#             project_name,
#             board["name"]
#         ) == 201

#     for board in ry.get_project_boards():
#         for lists in board["Lists"]:
#             assert gl.create_board_list(
#                 project_name,
#                 board["name"],
#                 lists
#             ) == 201
