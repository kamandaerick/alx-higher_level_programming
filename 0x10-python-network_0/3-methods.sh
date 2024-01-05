#!/bin/bash
# Take in a URL and display all HTTP methods the server will accept
curl -sI "$1" | awk '/^Allow/ { for (i=3; i<=NF; i++) print $i }'
