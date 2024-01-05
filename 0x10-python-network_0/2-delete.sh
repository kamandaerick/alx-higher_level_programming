#!/bin/bash
#send a DELETE request to provided URL passed as arg
#display the body of the response
curl -sX DELETE "$1"
