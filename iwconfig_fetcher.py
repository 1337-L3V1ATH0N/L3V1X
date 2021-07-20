#! /usr/bin/python3

import subprocess
import time

print('''\n\n\t\t===== Wireless Net Fetcher =====\n\n''')
	
ifcon = subprocess.check_output(['iwconfig']).decode('utf-8').split('\n')
	
for value in ifcon:
	
	if 'wlan0mon' in value:
		print('\n[+] Interface :',value.split(' ')[0],'\n\n[+]',value.split(' ')[5])		
	
	if 'wlan0' in value:
		print('\n[+]',value.split(' ')[8])
	if 'Mode' in value:
		print('\n[+]',value.split(' ')[10])
	if 'Access Point: Not-Associated' in value:
		print('\n[!] Not Connected to any device !')
		break
	if 'Access Point' in value:
		print('\n[+]',value.split(':')[2][-12:],':',value.split(' ')[-4])
		print()

