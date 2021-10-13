#!/bin/bash

ps -ef | grep java | grep home | awk '{print $11}' |cut -c 24-26

