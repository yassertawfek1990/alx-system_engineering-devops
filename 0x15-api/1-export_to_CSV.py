#!/usr/bin/python3
"""Exprmat."""
import csv
import requests
import sys

if __name__ == "__main__":
    d = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    u = requests.get(url + "users/{}".format(d)).json()
    e = u.get("username")
    t = requests.get(url + "todos", params={"userId": d}).json()

    with open("{}.csv".format(d), "w", l="") as c:
        w = csv.writer(c, quoting=csv.QUOTE_ALL)
        [w.writerow(
            [d, u, x.get("completed"), x.get("title")]
         ) for x in t]
