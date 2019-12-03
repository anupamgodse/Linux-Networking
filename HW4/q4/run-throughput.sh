#!/bin/bash

plugin=$1

for i in {1..10}
do
 kubectl apply -f iperf-server.yaml
 sleep 20
 kubectl apply -f iperf-client-job.yaml
 sleep 310
 kubectl logs -l app=iperf-overlay-server > logs/${plugin}_${i}_server.log
 kubectl logs -l app=iperf-overlay-client > logs/${plugin}_${i}_client.log
 kubectl delete -f iperf-server.yaml
 kubectl delete -f iperf-client-job.yaml
done
