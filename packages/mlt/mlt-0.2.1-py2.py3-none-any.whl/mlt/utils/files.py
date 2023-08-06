#
# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: EPL-2.0
#

import json
import os


def fetch_action_arg(action, arg):
    """fetches data from command json files"""
    action_json = '.{}.json'.format(action)
    if os.path.isfile(action_json):
        with open(action_json) as f:
            return json.load(f).get(arg)


def is_custom(target):
    custom = False
    if os.path.isfile('Makefile'):
        with open('Makefile') as f:
            for line in f:
                if line.startswith(target):
                    custom = True
                    break
    return custom
