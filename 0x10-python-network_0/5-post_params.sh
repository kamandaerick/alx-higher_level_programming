#!/bin/bash
#send a POST request to the passed URL, and display the body of the response
curl -sX POST -H "Content-Type: application/json" -d '{"email": "test@gmail.com", "subject": "I will always be here for PLD"}' "$1"
