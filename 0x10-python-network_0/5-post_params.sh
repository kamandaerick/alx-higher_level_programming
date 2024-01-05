#!/bin/bash
#send a POST request to the passed URL, and display the body of the response
curl -sX POST "email=test@gmail.com&subect=I will always be here for PLD" "$1" 
