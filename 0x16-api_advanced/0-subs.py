#!/usr/bin/python3
"""F."""
import requests


def number_of_subscribers(subreddit):
    """R."""
    u = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    h = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    r = requests.get(u, headers=h, allow_redirects=False)
    if r.status_code == 404:
        return 0
    s = r.json().get("data")
    return s.get("subscribers")
