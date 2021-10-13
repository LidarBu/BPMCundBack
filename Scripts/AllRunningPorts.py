import os

from Scripts.SSHClient import SSHClient


def exe(bpm_num):
    dir_name = os.path.dirname(__file__)
    path = os.path.join(dir_name, "AllRunningPorts.sh")
    ssh_client = SSHClient()
    return ssh_client.execute_script(path)
