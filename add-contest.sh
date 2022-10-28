#!/bin/bash

if [ "$#" -lt 2 ]; then
    echo "Not enough arguments. Usage: $0 <contest> <BOJ link>"
    exit -1
fi

printf '%s\n' "$1" > tmp.txt
curl -sS "$2" | pup '.table td:nth-child(3) json{}' | jq -r '.[] | .children | if . == null then [{}] else . end | .[] | map_values(sub("/problem/(?<n>[0-9]+)"; "\(.n)")) | [null, .href, .text] | @tsv' >> tmp.txt
prev_pattern=$((cat problems.txt | grep -v $'^\t' && printf '%s\n' "$1") | sort -r | grep -A 1 "$1" | tail -n 1)
sed -i '' '1s/^/\n/' problems.txt
ln=$(cat problems.txt | grep -n "$prev_pattern" | awk -F: '{print $1 - 1}')
sed -i '' "${ln}r tmp.txt" problems.txt
sed -i '' '1d' problems.txt 
rm tmp.txt
