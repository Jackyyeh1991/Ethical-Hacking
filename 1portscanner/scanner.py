#! /bin/python3

import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4
	# need to refine the input examination
else:
	print("invalid amout of argument")
	print("syntax: python3 scanner.py <ip>")

#Add a pretty banner
print("-"*50)
print(f'scanner target: {target}')
print(f'Time started: {str(datetime.now())}')
print("-"*50)


try:
	for port in range(50,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		if result == 0:
			print(f'Port {port} is open.')
		s.close()

except	KeyboardInterrupt:
	print("\n Exiting program.")
	sys.exit()

except socket.gaierror:
	print("\n Hostname cannot be resolved.")
	sys.exit()
	
except socket.error:
	print("\n Cannot connect to server")
	sys.exit()
