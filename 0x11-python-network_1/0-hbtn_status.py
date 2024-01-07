#!/usr/bin/python3
"""Fetch the following url https://alx-intranet.hbtn.io/status"""
import urllib.request


def fetch_status(url):
    with urllib.request.urlopen(url) as response:
        data = response.read()
        decoded_data = data.decode('utf-8')

        """Displaying the body of the response"""
        print("Body response:")
        print("\t- type: {}".format(type(data)))
        print("\t- content: {}".format(data))
        print("\t- utf8 content: {}".format(decoded_data))


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    fetch_status(url)
