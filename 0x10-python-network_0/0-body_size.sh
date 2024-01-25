#!/bin/bash
#use curl to display the size of a request

response=$(curl -s -o /dev/null -w "%{size_download}\n" "$1")
echo $response
