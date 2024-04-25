#!/bin/bash
# takes in a URL, sends a GET request to the URL, and displays the body of the response
response_body=$(curl -s -o -I -L -w "%{http_code}" "$1" | awk 'NR==1{status=$NF} NR>1 && status==200'); if [[ $response_body == "200" ]]; then curl -s "$1"; fi
