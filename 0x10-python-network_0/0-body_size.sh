#!/bin/bash
response_size=$(curl -s -o /dev/null -w "%{size_download}" "$1")
echo $response_size
