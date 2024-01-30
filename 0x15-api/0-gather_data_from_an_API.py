#!/usr/bin/python3
import requests

"""
this scripts fcetches and uses data from an api
"""


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
        completed_tasks = [x for x in tasks if x.get('completed')]
        print('Employee {} is done with tasks({}/{}):'.format(
            user.get('name'), len(completed_tasks), len(tasks)
        ))
        for x in completed_tasks:
            print('\t {}'.format(x.get('title')))
    except Exception as e:
        print('{}'.format(e))


if __name__ == "__main__":
    import sys
    user_id = int(sys.argv[1])
    print_tasks(user_id)
