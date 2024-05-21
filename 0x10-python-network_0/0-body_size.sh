#!/bin/bash
# takes in a URL, sends a GET request to the URL, and displays the body of the response
response_size=$(curl -s -o /dev/null -w "%{size_download}" "$1"); echo $response_size
