# PROJECT EXTRACT IP

interface = '''enp0s31f6: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.0.13  netmask 255.255.255.0  broadcast 192.168.0.255
        inet6 fe80::d250:99ff:fe8a:c5cb  prefixlen 64  scopeid 0x20<link>
        inet6 fda5:6bca:6bd1:14d:d250:99ff:fe8a:c5cb  prefixlen 64  scopeid 0x0<global>
        ether d0:50:99:8a:c5:cb  txqueuelen 1000  (Ethernet)
        RX packets 3264549  bytes 3207905582 (3.2 GB)
        RX errors 0  dropped 5769  overruns 0  frame 0
        TX packets 616138  bytes 531820141 (531.8 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
        device interrupt 16  memory 0xdf100000-df120000
'''
interface_list = interface.splitlines()
# print(interface_list)
addr_list = list()

for line in interface_list[1:5]:
    # print(line)
    tmp_list = line.split()
    # print(tmp_list)
    addr_list.append(tmp_list[1])
addr_list_str = ','.join(addr_list)
print(addr_list_str)
