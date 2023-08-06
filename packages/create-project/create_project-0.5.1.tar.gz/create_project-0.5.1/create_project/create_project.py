# -----------------------------------------------------------------------------
# Created: Sun 12 Aug 2018 19:16:32 IST
# Last-Updated: Mon 13 Aug 2018 02:52:25 IST
#
# create_project.py is part of create_project
# URL: https://gitlab.com/justinekizhak/create_project
# Description:
#
# Copyright (c) 2018, Justine Kizhakkinedath
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


def create_complete_project(file_name):
    ry.yaml_file_name = file_name

    # ry.print_file()
    project_name = ry.get_project_name()
    payload_data = {
        "name": project_name,
        "description": ry.get_project_description(),
        "visibility": ry.get_project_visibility()
    }
    print("Creating project...")
    if (gl.get_project_id(project_name) == None):
        gl.create_gitlab_project(payload_data)
    else:
        print("Project already exists.")

    print("Done. Creating labels...")
    for label in ry.get_project_labels():
        gl.create_project_labels(project_name, {
            "name": label["name"],
            "color": label["color"],
            "priority": label["priority"]
        })

    print("Done. Creating project boards...")
    for board in ry.get_project_boards():
        gl.create_project_board(project_name, board["name"])

    print("Done. Creating lists inside the boards...")
    for board in ry.get_project_boards():
        for lists in board["Lists"]:
            gl.create_board_list(project_name, board["name"], lists)
