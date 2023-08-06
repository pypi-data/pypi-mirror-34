#!/usr/bin/env python3
# -----------------------------------------------------------------------------
# Created: Sun 15 Jul 2018 19:12:54 IST
# Last-Updated: Mon 13 Aug 2018 01:58:16 IST
#
# __main__.py is part of create-project
# URL: https://gitlab.com/justinethomas/create-project
# Description: Endpoint
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

import argparse
from create_project import create_project as cp


def main(args=None):
    """The main routine."""
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'file_name',
        help="name of the yaml file",
        nargs='?',
        default="install.yaml")
    args = parser.parse_args()
    print("Creating your project on GitLab using", args.file_name, "...")
    cp.create_complete_project(args.file_name)

    print("All done.")


if __name__ == "__main__":
    main()
