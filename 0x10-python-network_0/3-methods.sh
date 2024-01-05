#!/bin/bash
# Display all HTTP a server accepts
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
