#!/usr/bin/python3
'''Display the value of the X-Request-Id'''
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    print(response.headers['X-Request-Id'])
