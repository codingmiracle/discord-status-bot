import subprocess
import platform
import socket
import sys

from jproperties import Properties

config = Properties()
with open('settings.properties', 'rb') as config_file:
    config.load(config_file)

def get_bot_token():
    result = config.get("bot-token")[0]
    if result:
        return result
    print("Set your Bot Token in `settings.properties`")
    sys.exit()

def get_ip():
    try:
        ip = subprocess.check_output(['hostname', '-I']).decode('UTF-8')
    except:
        hostname = socket.gethostname()
        ip = str(socket.gethostbyname(hostname))
    return ip

def get_hostname():
    try:
        hostname = socket.gethostname()
    except:
        hostname = subprocess.check_output(['hostname']).decode('UTF-8')
    return hostname

class ServiceRunner:
    def __init__(self):
        self.home = config.get("DefaultHomeDirectory")
        self.stdout = subprocess.PIPE
        self.stderr = subprocess.PIPE
        self.errors = ""
        process = subprocess.Popen(['cd', self.home], stdout=self.stdout, stderr=self.stderr)

    def run_returnable(self, command):
        try:
            process = subprocess.Popen(command.split(" "), stdout=self.stdout, stderr=self.stderr)
        except:
            return "error running command"
        stdout, self.errors = process.communicate()
        return stdout.decode("UTF-8")
