#!/usr/bin/python3
'''
Returns the number of subscribers for a give subrddit
'''
import requests


def number_of_subscribers(subreddit):
    '''
    Return number of subreddit subscribers
    '''
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    user_agent = 'reddit_user'

    headers = {'User-Agent': "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}

    req = requests.get(url, headers=headers, allow_redirects=False)

    if req.status_code == 404:
        return 0

    result = response.json().get("data")

    return result.get("subscribers")
