#!/bin/bash
# takes in a URL, sends a POST request to the passed URL, and displays the body of the response
response_body=$(curl -s -H "X-School-User-Id: 98" "$1") && echo "$response_body"
