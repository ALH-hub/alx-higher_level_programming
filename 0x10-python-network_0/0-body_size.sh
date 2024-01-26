#!/bin/bash
#use curl to display the size of a request
curl -s "$1" | wc -c
