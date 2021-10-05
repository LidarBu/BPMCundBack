import logging
import paramiko
from paramiko.ssh_exception import SSHException

import Configuration


class InitializeSSHClient:
    connected = False

    def __init__(self):
        configuration = Configuration()
        configuration.conf[""]

        try:
            private_key_path = configuration["PRIVATE_KEY_PATH"]
            self.host_name = configuration["HOST_NAME"]
        except Exception:
            logging.warning("Missing Configuration")

        self.private_key = paramiko.RSAKey.from_private_key_file(private_key_path)
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)

    def connect(self):
        if self.connected:
            return False, "The Client Already Connected"

        else:
            try:
                self.ssh.connect(hostname=self.host_name, pkey=self.private_key)
                self.connected = True
                return False
            except SSHException:
                return False

    def execute_command(self, command):
        ssh_stdin, ssh_stdout, ssh_stderr = self.ssh.exec_command(command)
        return ssh_stdin, ssh_stdout, ssh_stderr
