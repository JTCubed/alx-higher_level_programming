#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept.
allowed_methods=$(curl -s -X OPTIONS -I "$1" | grep "Allow:" | awk '{print substr($0, index($0,$2))}'); echo $allowed_methods
