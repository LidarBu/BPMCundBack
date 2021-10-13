#!/bin/bash
BPM_PROC=$(ps -ef | grep bpm{arg1} | grep java | awk '{print $2}')
netstat -nap 2>&1 | grep $BPM_PROC | grep LISTE | awk {'print $4'} | cut -d : -f 2
