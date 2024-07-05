#!/usr/bin/python3
'''Send a request to the URL and displays the body
of the response (decoded in utf-8'''
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        response = urllib.request.urlopen(url)
        print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as error:
        print(error.code)
