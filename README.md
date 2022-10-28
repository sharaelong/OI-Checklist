# OI-Checklist

Description
- run.sh: generate index.html
- add-contest.sh: add contest to problems.txt
- problems.txt: problem database. It has special format and sorted in reverse order of contest name.

Usage
```
./run.sh <BOJ handle>
```

Details of problems.txt and its modification method will be added soon.

Prerequisite

It uses third party library: jq, pup.
Also needs Python 3.
```
sudo apt-get install jq pup
```
