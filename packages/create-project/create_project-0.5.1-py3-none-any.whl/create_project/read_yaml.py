# -----------------------------------------------------------------------------
# Copyright (c) 2018, Justine Kizhakkinedath
# All rights reserved
#
# Licensed under the terms of MIT License
# See LICENSE file in the project root for full information.
# -----------------------------------------------------------------------------

import yaml
import os

yaml_file_name = "install.yaml"


def read_file():
    if os.path.exists(yaml_file_name):
        with open(yaml_file_name) as fp:
            my_configuration = yaml.load(fp)
            return (my_configuration)
    else:
        print("File not found")


def print_file():
    if os.path.exists(yaml_file_name):
        with open(yaml_file_name) as fp:
            my_configuration = yaml.load(fp)
            print(my_configuration)
    else:
        print("File not found")


def get_project_name():
    data = read_file()
    return (data["name"])


def get_project_description():
    data = read_file()
    return (data["description"])


def get_project_visibility():
    data = read_file()
    return (data["visibility"])


def get_project_labels():
    data = read_file()
    return (data["Labels"])


def get_project_boards():
    data = read_file()
    return (data["Boards"])
