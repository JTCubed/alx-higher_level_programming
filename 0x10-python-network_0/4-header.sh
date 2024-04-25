#!/bin/bash

response_body=$(curl -s -H "X-School-User-Id: 98" "$1")

echo "$response_body"
