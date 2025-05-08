import sys
import socket

# aim : create a port scanner 

def scan_ports(target_ip):

    banner = " PORT SCANNER STARTING ---- "
    print(banner)
    
    try:
        for port in range(1,65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = s.connect_ex((target_ip, port))

            if(result == 0):
                print(f" => port open -- {port}")

        
    except KeyboardInterrupt:
        print(" Keyboard interrupt identified --- exiting ")
        sys.exit()
    
    except:
        print("unknown error encountered")
        sys.exit()


ip = input(str("enter the target ip : "))
scan_ports(ip)