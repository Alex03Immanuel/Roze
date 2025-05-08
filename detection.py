#usr/bin/python3
#sample comment

# /// import necessary modules ///

import sys
import time
import os
import nmap

# operating system scans

os.system("ipconfig")


print("give the ip adress")
target_ip = input("ENTER HERE : ")


def OSscan(target_ip):

    nm = nmap.PortScanner(nmap_search_path=('C:\\Program Files (x86)\\Nmap\\nmap.exe',))
    nm.scan(target_ip,arguments='-O')

    if target_ip in nm.all_hosts():

        print(f"HOST : {target_ip}")
        print(f"STATE : {nm[target_ip].state()}")

    else:

        print("detection failed")


OSscan(target_ip)