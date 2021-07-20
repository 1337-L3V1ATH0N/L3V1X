#! /usr/bin/python3

import os
import subprocess
import time
file_time = 7
try:
	for file in os.listdir():
		if '/L3V1X' not in os.getcwd():
			print('\n[ERROR] Check your current directory using \'pwd\'!\nIt should be inside L3V1X folder!\n')
			break
		if 'install.py' in file:
			pass
		
		elif '.py' in file:	
			os.system('clear')
			print('Installing L3V1X... Have Patience')
			print('Installation progress :',int(file_time))
			time.sleep(1)
			subprocess.call('sudo cp '+file+' /usr/bin/',shell=True)
			file_time+=5.2
			
	else:
		print('\n\t\tReady to use. Use \'L3V1X.py\' to run the tool !')
except:
	print('\n[ERROR] Encountered Error !')
	pass
