#!/usr/bin/python3
"""Exportformat."""
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    la = "https://jsonplaceholder.typicode.com/"
    u = requests.get(la + "users/{}".format(user_id)).json()
    n = u.get("username")
    t = requests.get(la + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as j:
        json.dump({user_id: [{
                "task": x.get("title"),
                "completed": x.get("completed"),
                "username": n
            } for x in t]}, j)
