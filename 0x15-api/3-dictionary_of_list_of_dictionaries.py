#!/usr/bin/python3
"""
this scripts fcetches and uses data from an api
"""
import json
import requests


def print_tasks():
    """
    this script print users details
    """
    data_to_be_written = {}
    for x in range(1, 11):
        try:
            tasks_response = requests.get(
                'https://jsonplaceholder.typicode.com/users/{}/todos'
                .format(x))
            user_response = requests.get(
                'https://jsonplaceholder.typicode.com/users/{}'.format(x))
            tasks = tasks_response.json()
            user = user_response.json()
            username = user.get('username')
            list_tasks = [
                {"username": username,
                 "task": task.get('title'),
                 "completed": task.get('completed')}
                for task in tasks]
            data_to_be_written.update({"{}".format(x): list_tasks})
            # print(data_to_be_written)
            # for task in list_tasks:
            #     print(task)
        except Exception as e:
            print('{}'.format(e))
    filename = 'to_do_all_employees.json'
    with open(filename, 'w') as jsonfile:
        json.dump(data_to_be_written, jsonfile)


if __name__ == "__main__":
    print_tasks()
