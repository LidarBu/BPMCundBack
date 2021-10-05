import platform
import subprocess
import json
import logging
import os
from functools import partial

linux_command = 'ssh {USER}@{SERVER} \'bash -s\' < tail -100 {LOG_HOME}/{BPM}/{FILE_NAME}'
windows_command = 'ssh {USER}@{SERVER} \'bash -s\' < tail -100 {LOG_HOME}/{BPM}/{FILE_NAME}'

plat = platform.system()
command = ''

if plat == 'Linux':
    command = linux_command
elif plat == 'Windows':
    command = windows_command

dir_name = os.path.dirname(__file__)
path = os.path.join(dir_name, "../config/settings.json")

with open(path, "r") as file:
    configuration = json.load(file)

USER = ''
SERVER = ''
LOG_HOME = ''

try:
    USER = configuration["USER"]
    SERVER = configuration["SERVER"]
    LOG_HOME = configuration["LOG_HOME"]
except Exception:
    logging.warning("Missing Configuration")

print(command)


def exe(bpm_num):
    formatted_command = command.format(USER, SERVER, LOG_HOME, bpm_num, "bpm" + bpm_num + ".log")
    p = subprocess.Popen(formatted_command, stdout=subprocess.PIPE)
    output, err = p.communicate()
    return output, err
