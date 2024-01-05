#!/bin/bash
#accept a url, send a request
#display the sie of the body in bytes
url="$1"

response=$(curl -sI "$url")

#content length
content_length=$(echo "$response" | grep -i '^Content-Length:' | tr -d '\r' | awk '{print $2}')

#display the content length in bytes
echo ${content_length}

