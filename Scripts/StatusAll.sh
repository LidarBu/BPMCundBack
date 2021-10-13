#!/bin/bash

GREEN=$(tput setaf 2)
RED=$(tput setaf 3)
reset=$(tput sgr0)
INSTALLED_BPMS=$(ls -d $SOA_BASE/bpm[1-9]*)
FLAG=0
for i in $(echo $INSTALLED_BPMS); do
  a=$(basename $i)
  ps -ef | grep java | grep random | grep $a 2>&1 >/dev/null
  if [ $? -ne 0 ]; then
    echo "${RED}$a IS NOT RUNNING${reset}"
    FLAG=1
  fi
done
if [ $FLAG -eq 0 ]; then
  echo "${GREEN}ALL GOOD - All BPMs are up and running${reset}"
  #echo "List:"
  #echo " $INSTALLED_BPMS"
fi
