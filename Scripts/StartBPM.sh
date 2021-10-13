#!/bin/bash
echo "starting bpm{arg1}"
nohup java -jar -Djava.security.egd=file:/dev/urandom /home/cmlapp/pessoa/bpm$1/target/bpm{arg1}.jar 2>&1 >>/home/cmlapp/pessoa/bpm{arg1}/bpm{arg1}.log &
