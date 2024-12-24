# -*- encoding: utf-8 -*-
"""
    @File : ins_function.py \n
    @Contact : yafei.wang@pisemi.com \n
    @License: (C)Copyright {} \n
    @Modify Time: 2023/11/20 10:04 \n
    @Author : Pisemi Yafei Wang \n
    @Version: 1.0 \n
    @Description : None \n
    @Create Time: 2023/11/20 10:04 \n
"""

import json
import pkg_resources

def register_function(pInsType, pInsName):
    """
    register the instrument function
    :param pInsType: instrument type
    :param pInsName: instrument name
    :return: command
    """

    # Use pkg_resources to get the path to the JSON file
    try:
        json_file = pkg_resources.resource_filename(__name__, 'ins.json')
    except Exception as e:
        print(f"Error locating JSON file: {e}")
        return None

    # Read and parse the JSON file
    try:
        with open(json_file, 'r') as f:
            command = json.load(f)
    except FileNotFoundError:
        print("JSON file not found.")
        return None
    except json.JSONDecodeError:
        print("Error decoding JSON file.")
        return None

    # Find and return the command
    if pInsType in command:
        for j in command[pInsType]:
            if pInsName.startswith(j[:3]):
                print(command[pInsType][j])
                return command[pInsType][j]

    print("No matching command found.")
    return None