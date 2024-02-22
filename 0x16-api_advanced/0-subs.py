#!/usr/bin/python3
'''this module finds the total number of  subscribers in a subredit'''
import requests


def number_of_subscribers(subreddit):
    """
    Retrieves the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mordecai"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0
