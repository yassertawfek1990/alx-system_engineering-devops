#!/usr/bin/python3
"""Ext."""
import json
import requests

if __name__ == "__main__":
    urla = "https://jsonplaceholder.typicode.com/"
    s = requests.get(urla + "users").json()

    with open("todo_all_employees.json", "w") as j:
        json.dump({
            x.get("id"): [{
                "task": c.get("title"),
                "completed": c.get("completed"),
                "username": x.get("username")
            } for c in requests.get(urla + "todos",
                                    params={"userId": x.get("id")}).json()]
            for x in s}, j)
