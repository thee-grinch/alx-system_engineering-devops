#!/usr/bin/python3
"""
this is a pthon request
"""
import requests


def top_ten(subreddit):
    '''This function queries the Reddit API and prints the titles of the'''
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        
        for post in posts:
            title = post["data"]["title"]
            print(title)
    else:
        print(None)