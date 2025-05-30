import asyncio
import asyncssh

async def run_client(host, username, password, command):
    async with asyncssh.connect(host=host, username=username, password=password, known_hosts=None) as connection:
        return await connection.run(command)

async def run_multiple_clients(hosts):
    tasks = list()
    for host in hosts:
        task = run_client(host['host'], host['username'], host['password'], host['command'])
        tasks.append(task)

    results = await asyncio.gather(*tasks, return_exceptions=True)

    i = 0
    for result in results:
        i += 1
        if isinstance(result, Exception):
            print(f'Task {i} failed: {str(result)}')
        elif result.exit_status != 0:
            print(f'Task {i} exit status: {result.exit_status}')
            print(result.stderr, end='')
        else: 
            print(f'Task {i} succeeded:')
            print(result.stdout, end='')
        print('#' * 50)

hosts = [
    {'host': '172.16.0.1',
     'username': 'admin',
     'password': 'admin',
     'command': 'dir'
     },
     {'host': '172.16.0.2',
     'username': 'admin',
     'password': 'admin',
     'command': 'dir'
     },
     {'host': '172.16.0.3',
     'username': 'admin',
     'password': 'admin',
     'command': 'dir'
     }
]

asyncio.run(run_multiple_clients(hosts))
