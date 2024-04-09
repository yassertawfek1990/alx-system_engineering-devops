#!/usr/bin/python3
"""F"""
import requests


def top_ten(subreddit):
    """t."""
    u = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    h = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    p = {
        "limit": 10
    }
    r = requests.get(u, headers=h, params=p,
                            allow_redirects=False)
    if r.status_code == 404:
        print("None")
        return
    s = r.json().get("data")
    [print(v.get("data").get("title")) for v in s.get("children")]
