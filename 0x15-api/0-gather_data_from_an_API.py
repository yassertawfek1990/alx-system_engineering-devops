#!/usr/bin/python3
"""ReD."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    E = requests.get(url + "users/{}".format(sys.argv[1])).json()
    T = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    N = [x.get("title") for x in T if x.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        E.get("name"), len(N), len(T)))
    [print("\t {}".format(x)) for x in N]
