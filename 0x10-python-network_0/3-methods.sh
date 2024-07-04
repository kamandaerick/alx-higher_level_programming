#!/bin/bash
#Display only accepted http methods
curl -s -i -X OPTIONS "$1" | grep -i 'Allow:' | awk '{print $2}'
