#!/usr/bin/python3
"""ReD."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    EMPLOYEE_NAME = requests.get(url + "users/{}".format(sys.argv[1])).json()
    TOTAL_NUMBER_OF_TASKS = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    NUMBER_OF_DONE_TASKS = [x.get("title") for x in TOTAL_NUMBER_OF_TASKS if x.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME.get("name"), len(NUMBER_OF_DONE_TASKS), len(TOTAL_NUMBER_OF_TASKS)))
    [print("\t {}".format(x)) for x in NUMBER_OF_DONE_TASKS]
