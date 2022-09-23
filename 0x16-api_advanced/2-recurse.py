#!/usr/bin/python3
"""
Write a recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit. If no
results are found for the given subreddit, the function should return None
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ If not a valid subreddit, return None """
    try:
        api_url = 'https://www.reddit.com/r/{}/hot.json'.format(
            subreddit)
        response = requests.get(
            api_url, headers={"User-Agent": "Mozilla/5.0"},
            params={'after': after}, allow_redirects=False)
        children = response.json()['data']['children']
        for title in children:
            hot_list.append(title['data']['title'])
        after = response.json()['data']['after']
        if after is not None:
            recurse(subreddit, hot_list, after)
        return hot_list
    except Exception:
        return None
