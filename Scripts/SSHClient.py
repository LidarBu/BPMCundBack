import json
import logging
import paramiko
from paramiko.ssh_exception import SSHException

import Configuration


class SSHClient:
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

    def __connect(self):
        if self.connected:
            return False, "The Client Already Connected"

        else:
            try:
                self.ssh.connect(hostname=self.host_name, pkey=self.private_key)
                self.connected = True
                return True
            except SSHException:
                return False

    def __disconnect(self):
        if not self.connected:
            return False, "The client is not connected"
        else:
            self.ssh.close()
            self.connected = False
            return True, "Disconnect the client"

    def execute_command(self, command):
        self.__connect()
        ssh_stdin, ssh_stdout, ssh_stderr = self.ssh.exec_command(command)
        self.__disconnect()
        return ssh_stdin, ssh_stdout, ssh_stderr

    def execute_script(self, path):
        self.__connect()
        with open(path, "r") as file:
            script = json.load(file)
        ssh_stdin, ssh_stdout, ssh_stderr = self.ssh.exec_command(script)
        self.__disconnect()
        return ssh_stdin, ssh_stdout, ssh_stderr
