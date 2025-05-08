# Detectiob of OS

import platform

def detection():
    
	plt_lst = [platform.system(),platform.release()]
    
	print(platform.system())
    
	print(platform.release())
    
	if plt_lst[0] == "Windows":
		return 1
	elif plt_lst[0] == "Linux":
		return 0
	else:
		return 1

os_res = detection()
print(os_res)
    

