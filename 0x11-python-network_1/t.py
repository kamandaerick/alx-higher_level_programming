#!/usr/bin/python3
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        X_id = dict(response.headers)
        print(X_id.get("X-Request-Id"))
