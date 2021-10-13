import os

from Scripts.SSHClient import SSHClient


def exe():
    dir_name = os.path.dirname(__file__)
    path = os.path.join(dir_name, "StatusAll.sh")
    ssh_client = SSHClient()
    return ssh_client.execute_script(path)
