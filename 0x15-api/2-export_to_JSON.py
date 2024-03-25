#!/usr/bin/python3
"""Ext."""
import json
import requests

if __name__ == "__main__":
    la = "https://jsonplaceholder.typicode.com/"
    u = requests.get(la + "users").json()

    with open("todo_all_employees.json", "w") as j:
        json.dump({
            x.get("id"): [{
                "task": c.get("title"),
                "completed": c.get("completed"),
                "username": u.get("username")
            } for c in requests.get(la + "todos",
                                    params={"userId": x.get("id")}).json()]
            for x in u}, j)
