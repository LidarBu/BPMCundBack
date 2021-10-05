import platform
import subprocess
import json
import logging
import os

import paramiko

from Scripts.InitializeSSHClient import InitializeSSHClient



def exe():
    ssh_client = InitializeSSHClient()
    ssh_client.connect()



