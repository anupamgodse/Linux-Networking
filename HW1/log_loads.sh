#!/bin/sh

#GRANULARITY
T=$1

#Total time
TP=$2

#High CPU Usage threshold
X=$3

#Very High CPU Usage threshold
Y=$4

LOOPS=$((TP / T))

last_la1=-1
increasing=

while [ "$LOOPS" -gt 0 ]
do
  #populate log file	
  timestamp=$(date)
  load_avgs=$(uptime | grep -o 'load.*' | cut -d ':' -f 2)
  echo $timestamp $load_avgs >> $HOME/load.csv

  #Generate alerts
  la1=$(echo $load_avgs | cut -d ',' -f 1)
  la5=$(echo $load_avgs | cut -d ',' -f 2)
  la15=$(echo $load_avgs | cut -d ',' -f 3)

  if [ $(echo "$la1 > $last_la1" | bc) -eq 1 ] && [ $(echo "$last_la1 != -1" | bc) -eq 1 ]; then
    increasing=1
  else
    increasing=0
  fi

  last_la1=$la1

  if [ $( echo "$la1 > $X" | bc ) -eq 1 ]; then
    echo $timestamp "HIGH CPU usage" $load_avgs >> $HOME/load_alerts.csv
  fi

  if [ $( echo "$la5 > $Y" | bc ) -eq 1 ] && [ $increasing -eq 1 ]; then
    echo $timestamp "Very HIGH CPU usage" $load_avgs >> $HOME/load_alerts.csv
  fi
    
  #wait for $T secs
  sleep $T

  LOOPS=$((LOOPS-1))
done
