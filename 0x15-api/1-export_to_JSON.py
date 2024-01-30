#!/usr/bin/python3
"""
this scripts fcetches and uses data from an api
"""
import json
import requests


def print_tasks(user_id):
    """
    this script print users details
    """
    try:
        tasks_response = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}/todos'
            .format(user_id))
        user_response = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(user_id))
        tasks = tasks_response.json()
        user = user_response.json()
        username = user.get('username')
        list_tasks = [
            {"task": task.get('title'),
             "completed": task.get('completed'), "username": username} for task in tasks]
        filename = '{}.json'.format(user_id)
        data_to_be_written = {"{}".format(user_id): list_tasks}
        # print(data_to_be_written)
        with open(filename, 'w') as jsonfile:
            json.dump(data_to_be_written, jsonfile)
        # for task in list_tasks:
        #     print(task)
    except Exception as e:
        print('{}'.format(e))


if __name__ == "__main__":
    import sys
    user_id = int(sys.argv[1])
    print_tasks(user_id)
