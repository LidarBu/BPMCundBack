#!/bin/bash
for i in $(/home/cmlapp/bin/runningBPM.bash); do echo "bpm$i : $(/home/cmlapp/bin/portBPM.bash $i)"; done