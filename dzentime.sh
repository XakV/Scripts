#!/bin/bash

while :
do
  ETZdate=$(date "+%H:%M %Z")
  UTZdate=$(date -u "+%H:%M %Z")
  echo -e "$ETZdate  /n  $UTZdate"
  sleep 15s
done |
dzen2 -x 0 -y 0 -h 1080 -w 36 -p
