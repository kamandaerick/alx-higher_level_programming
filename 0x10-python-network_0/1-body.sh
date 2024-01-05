#!/bin/bash
#display the body of http get response
url=$1

response=$(curl -sIX GET "$url" | head -n 1 | awk '{print $2}')
content=$(curl -sX GET "$url")

if [ -n "$response" ] && [ "$response" -eq 200 ];
then
	echo "$content"
else
	echo "An error occured"
	exit 1
fi
