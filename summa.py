import nmap
import os

os.system("ifconfig")


print("give the ip adress")
target_ip = input("ENTER HERE : ")

nm = nmap.PortScanner()
nm.scan(target_ip,arguments='-O')