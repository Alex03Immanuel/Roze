# OPERATING SYSTEM DETECTION FOR A SINGLE IP

import nmap
import os

# DISPLAY YOUR CURRENT NETWORK SETTINGS 

os.system("ipconfig")

# SINGLE IP OS DETECTION SYSTEM - PHASE 1.1

def detect_os(target_ip):
    nm = nmap.PortScanner()

    print(f"Scanning {target_ip} for OS detection...")
    
    nm.scan(target_ip, arguments="-O")

    if 'osmatch' in nm[target_ip] and nm[target_ip]['osmatch']:
        os_needed = max(nm[target_ip]['osmatch'], key=lambda os:int(os['accuracy']))

        print(f"operating system is : {os_needed['name']}")
    else:
        print("OS detection failed. Try using root privileges.")

# IP TRANSFER FOR ALL THE NETWORK

def transform_ip(target_ip):
    
    os.system("arp -g")
    print('under development')

# NETWORK IP DETECTION SYSTEM - PHASE 1.2.2
        
def detect_network(network_ip):
    print('under development')


# BANNER

print("---------------------------------")
print("---------------------------------")
print()
print("SCANNER TYPE [0] : CUSTOM IP SEARCH")
print("---------------------------------")
print("SCANNER TYP [1] : ENTIRE NETWORK")
print()
print("---------------------------------")
print("---------------------------------")

# PROGRAM START 

scanner_type = int(input(" TYPE OF SCAN 0/1: "))

if(scanner_type == 0):
    print("--------------------------------")
    target_ip = input("enter the ip adress: ") 
    print("---------------------------------")

    detect_os(target_ip)

if(scanner_type == 1):
    print("--------------------------------")
    target_ip = input("enter the ip adress: ") 
    print("---------------------------------")


    network_ip = transform_ip(target_ip)
    detect_network(network_ip)


# sample comment 
