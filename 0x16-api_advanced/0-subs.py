#!/usr/bin/python3
"""How many subs?
This function queries subscribers on a given Reddit subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns
    the number of subscribers"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "AppleWebKit:0x16.api.advanced:v1.0.0 \
                       (by /u/JazzlikeFig4018)"
    }
    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code == 404:
        return 0
    results = res.json().get("data")
    return results.get("subscribers")
