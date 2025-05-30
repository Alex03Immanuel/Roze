# Detectiob of OS

import platform
import os
import subprocess
import ipaddress
import re

# finding the os of your own device

"""
def same_detection():
    
	plt_lst = [platform.system(),platform.release()]
    
	print(platform.system())
    
	print(platform.release())
    
	if plt_lst[0] == "Windows":
		return "Win"
	elif plt_lst[0] == "Linux":
		return "Lin"
	else:
		return "Unknown"
"""

# finding all the ip addresses 

active_ip_lst = []

def router_ip():

    x = os.system("ip route | grep -i 'default via' | awk '{print $3}'")
    result = subprocess.check_output("ip route | grep -i 'default via' | awk '{print $3}'", shell=True, text=True)
    result = result.strip()
    print(f"your local ip is : {result}")
    return result

def ping_all_ip(res):

    print("Working on it pls wait ... ")

    ip_net = res + "/24"
    network = ipaddress.ip_network(ip_net, strict=False)
    os_type = platform.system()
    
    for ip in network.hosts():
        ip = str(ip)
        if os_type == "Linux":
            result_term = subprocess.run(f"ping -c 1 -W 1 {ip}", shell=True, text=True, capture_output=True )
            if "1 received" in result_term.stdout:
                active_ip_lst.append(ip)
    return active_ip_lst     

def detection():
    for ip in active_ip_lst:
        
        subprocess.run(f"ping -c 1{ip}", shell = True, text = True, capture_output=True)
        ttl_ping = subprocess.run(f"ping -c 1 {ip}", shell = True, text = True)
        ttl = re.search(r'ttl = (\d+)', ttl_ping.stdout.lower())

        ttl_value = int(ttl.group(1))
        
        if(ttl_value == 64):
            return "Lin"

        else:
            return "Win"
        
# implement a dictionary {ip:os}
#bye bye



loc_ip = router_ip()
ping_all_ip(loc_ip)
detection(active_ip_lst)
print(active_ip_lst)


