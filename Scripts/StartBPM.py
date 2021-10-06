import platform
import subprocess
import json
import logging
import os

import paramiko

from Scripts.SSHClient import SSHClient


def exe(bpm_num):
    dir_name = os.path.dirname(__file__)
    path = os.path.join(dir_name, "../config/StartBPM.sh")
    ssh_client = SSHClient()

