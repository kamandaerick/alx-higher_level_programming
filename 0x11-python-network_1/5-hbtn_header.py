#!/usr/bin/python3
"""Send a request to the URL supplied as an argument
and display the value of X-Request-Id"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)

    for k, v in r.headers.items():
        if k == "X-Request-Id":
            print(v)
