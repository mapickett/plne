# Secure Copy

import paramiko
import getpass
from scp import SCPClient

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy())

# Connection credentials
password = getpass.getpass('Enter device password:')
router = {'hostname': '172.20.20.6',
          'username': 'admin',
          'password': password
}

ssh_client.connect(**router, look_for_keys=False, allow_agent=False)

scp = SCPClient(ssh_client.get_transport())

# Upload file from local host to remote server
scp.put('requirements.txt', '/tmp')

# Upload directory example
# scp.put('directory1', recursive=True, remote_path='/tmp')

# Download a file
scp.get('/entrypoint.sh', '/tmp')

scp.close()