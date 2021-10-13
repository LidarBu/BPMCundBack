#!/bin/bash
echo "stoping bpm {arg1}"
BPM_PROC=$(ps -ef | grep bpm{arg1} | grep java | awk '{print $2}')
kill -9 $BPM_PROC
