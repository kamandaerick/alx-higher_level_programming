#!/usr/bin/python3
"""Send a request to given url and display the body"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    if r.status_code > 400:
        print("Error code: ", r.statuscode)
