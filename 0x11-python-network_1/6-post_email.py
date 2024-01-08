#!/usr/bin/python3
"""Take in a URL and an email address, send a POST
    request with an email as a parameter and display
    the body
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    parameter = {"email": sys.argv[2]}

    r = requests.post(url, data=parameter)
    print(r.text)
