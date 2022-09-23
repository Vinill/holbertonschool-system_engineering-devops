#!/usr/bin/python3
"""
Write a recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit. If no
results are found for the given subreddit, the function should return None
"""
import requests


def top_ten(subreddit):
    """ If not a valid subreddit, print None """
    try:
        api_url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(
            subreddit)
        response = requests.get(
            api_url, headers={"User-Agent": "Mozilla/5.0"})
        response = response.json()['data']['children']
        for title in response:
            print(title['data']['title'])
    except Exception:
        print(None)
