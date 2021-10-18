import paramiko
from paramiko.ssh_exception import SSHException

from .Configuration import Configuration


class SSHClient:
    connected = False

    def __init__(self):
        configuration = Configuration()
        self.ssh = ' '

        private_key_path = configuration.conf["PRIVATE_KEY_PATH"]
        self.host_name = configuration.conf["HOST_NAME"]

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

    def execute_command(self, command, **kwargs):
        self.__connect()
        ssh_stdin, ssh_stdout, ssh_stderr = self.ssh.exec_command(command)
        ssh_stdout = ssh_stdout.readlines()
        ssh_stderr = ssh_stderr.readlines()
        self.__disconnect()
        return ssh_stdout, ssh_stderr

    def execute_script(self, path, **kwargs):
        self.__connect()
        with open(path, "r") as file:
            script = file.read()
        if kwargs is not None:
            script = str(script).format(**kwargs)
        print(script)

        ssh_stdin, ssh_stdout, ssh_stderr = self.ssh.exec_command(script)
        ssh_stdout = ssh_stdout.readlines()
        ssh_stderr = ssh_stderr.readlines()
        self.__disconnect()
        return ssh_stdout, ssh_stderr
