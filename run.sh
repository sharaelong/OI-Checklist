#!/bin/bash

if [ "$#" -lt 1 ]; then
    echo "Not enough arguments. Usage: $0 <BOJ handle>"
    exit -1
fi

cat <(curl -sS "https://www.acmicpc.net/user/$1" | pup '.panel-default:nth-child(2) a text{}' | tail -n +2) problems.txt | python3 main.py > index.html && open index.html
