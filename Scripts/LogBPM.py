import logging

from Scripts.Configuration import Configuration
from Scripts.SSHClient import SSHClient


def exe(bpm_num):
    command = 'tail -100 {LOG_HOME}/{BPM}/{FILE_NAME}'
    configuration = Configuration()

    LOG_HOME = ''

    try:
        LOG_HOME = configuration.conf["LOG_HOME"]
    except Exception:
        logging.warning("Missing Configuration")

    formatted_command = command.format(LOG_HOME=LOG_HOME, BPM=bpm_num, FILE_NAME="bpm" + bpm_num + ".log")
    print(formatted_command)
    ssh_client = SSHClient()
    ssh_stdout, ssh_stderr = ssh_client.execute_command(formatted_command)

    return ssh_stdout, ssh_stderr
