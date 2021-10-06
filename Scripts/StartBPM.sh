#!/bin/bash
echo "starting bpm$1"
nohup java -jar -Djava.security.egd=file:/dev/urandom  /home/cmlapp/pessoa/bpm$1/target/bpm$1*.jar 2>&1 >>  /home/cmlapp/pessoa/bpm$1/bpm$1.log &
