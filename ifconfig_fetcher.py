#! /usr/bin/python3

# Author : L3V1ATH0N urf : Akash Pandey

import subprocess
import time

banner = '''\n( $cR!P+ Wr!++3n 8y [ L3V1ATH0N a.k.a : Akash Pandey ] ! )\n'''
print(banner)
ifcon = subprocess.check_output(['ifconfig']).decode('utf-8').split('\n')

for value in ifcon:
		
	if 'inet6' in value:
		pass # don't include ip version 6

	elif 'eth0' in value:
		print('\nInterface =',value.split(' ')[0]) # gets the interface for ethernet lan cables.
		print(20*'-')
	elif 'ether' in value:
		print('\nMac Addr :',value.split(' ')[9:10]) # prints Mac Address of lan cable

	elif 'inet 127.0.0.1' in value:
		pass		# don't include loopback ip address

	elif 'inet' in value:
		print('\nIPv4 :',value.split(' ')[9:10]) # prints the ipv4 address

	elif 'wlan0' in value:
		print('\nInterface =',value.split(' ')[0]) # prints interface for wireless interface
		print(20*'-')
	elif 'ether' in value:
		print('\nMac Addr :',value.split(' ')[9:10]) # prints the mac address of wireless interface
