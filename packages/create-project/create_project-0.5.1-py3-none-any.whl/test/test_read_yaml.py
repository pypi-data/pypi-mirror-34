# -----------------------------------------------------------------------------
# Copyright (c) 2018, Justine Kizhakkinedath
# All rights reserved
#
# Licensed under the terms of MIT License
# See LICENSE file in the project root for full information.
# -----------------------------------------------------------------------------

from create_project import read_yaml


# # Works
# def test_read_file():
#     # print(read_yaml.read_file())
#     assert read_yaml.read_file()


# # Works
# def test_get_project_name():
#     assert read_yaml.get_project_names() == "Foo"


# # Works
# def test_get_project_description():
#     assert read_yaml.get_project_description() == "Some description"

# # Works
# def test_get_project_visibility():
#     assert read_yaml.get_project_visibility() == "public"

# # Works
# def test_print_label_colors():
#     assert read_yaml.get_project_labels()[0]["color"] == "#FF6347"

# # Works
# def test_get_project_boards():
#     assert read_yaml.get_project_board()[0]["name"] == "Board1"


# Works
def test_get_project_lists():
    for i in read_yaml.get_project_boards():
        print(i["Lists"])
