#!/usr/bin/python3
"""
this scripts fcetches and uses data from an api
"""
import csv
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
            [task.get('userId'), username, task.get('completed'),
             task.get('title')] for task in tasks]
        filename = '{}.csv'.format(user_id)
        with open(filename, 'w') as file:
            writer = csv.writer(file, quotechar='"', quoting=csv.QUOTE_ALL)
            writer.writerows(list_tasks)
    except Exception as e:
        print('{}'.format(e))


if __name__ == "__main__":
    import sys
    user_id = int(sys.argv[1])
    print_tasks(user_id)
