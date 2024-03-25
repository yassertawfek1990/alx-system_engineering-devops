#!/usr/bin/python3
"""Ext."""
import csv
import json
import requests
import sys


if __name__ == '__main__':
    d = sys.argv[1]
    la = 'https://jsonplaceholder.typicode.com/users/' + d
    r = requests.get(la)
    """Documentation"""
    n = r.json().get('username')
    """Documentation"""
    lt = la + '/todos'
    r = requests.get(lt)
    t = r.json()
    di = {d: []}
    for x in t:
        c = t.get('completed')
        h = t.get('title')
        di[d].append({
                                  "task": h,
                                  "completed": c,
                                  "username": n})
    """print(dict_data)"""
    with open('{}.json'.format(d), 'w') as z:
        json.dump(di, z)
