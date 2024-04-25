#!/bin/bash
response_body=$(curl -s -X DELETE "$1")
echo "$response_body"
