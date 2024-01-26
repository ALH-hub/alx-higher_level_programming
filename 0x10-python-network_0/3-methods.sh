#!/bin/bash
#display acceptable methods acceptable
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
