import time

class Device:

    def __init__(self, host, username, password, tn=None):
        self.host = host
        self.username = username
        self.password = password
        self.tn = tn

    def connect(self):
        import telnetlib
        self.tn = telnetlib.Telnet(self.host)
    
    def authenticate(self):
        self.tn.read_until(b'Username: ')
        self.tn.write(self.username.encode() + b'\n')
        self.tn.read_until(b'Password: ')
        self.tn.write(self.password.encode() + b'\n')

    def send(self, command, timeout=0.5):
        print(f'Sending command: {command}')
        self.tn.write(command.encode() + b'\n')
        time.sleep(timeout)

    def send_from_list(self, commands):
        for cmd in commands:
            self.send(cmd)
    
    def send_from_file(self, file):
        with open(file, 'r') as f:
            commands = f.read().splitlines()
            for cmd in commands:
                self.send(cmd)

    def show(self):
        output = self.tn.read_all().decode('UTF-8')
        return output
    
if __name__ == "__main__":

    routers= [
        {
            'host': '172.16.0.1',
            'username': 'admin',
            'password': 'admin',
            'loopback': '1.1.1.1'
        },
        {
            'host': '172.16.0.2',
            'username': 'admin',
            'password': 'admin',
            'loopback': '2.2.2.2'
        },
        {
            'host': '172.16.0.3',
            'username': 'admin',
            'password': 'admin',
            'loopback': '3.3.3.3'
        }
    ]

    commands = [
        'term len 0',
        'show ip int br',
        'exit'
    ]

    for router in routers:
        r = Device(
            host=router['host'],
            username=router['username'],
            password=router['password']
        )

        r.connect()
        r.authenticate()
        r.send_from_list(commands)
        print(r.show())