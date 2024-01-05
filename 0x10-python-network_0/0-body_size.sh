#!/bin/bash
#accept a url, send a request
#display the sie of the body in bytes
url="$1"

response=$(curl -sI "$url")

#content length
response_body=$(curl -sL -w "%{size_download}" "$url")
#display the content length in bytes
echo ${response_body}

