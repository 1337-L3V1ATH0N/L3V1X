#! /usr/bin/python3

import subprocess
import os
import time

login = os.getlogin()
node = os.uname()[1]

def banner():
	print('''\t\t\t=========================
\t\t\t+--|\tL3V1ATH0N    |--+
\t\t\t=========================\n\n''')	
os.system('clear')
banner()
while True:
	try:
		try:
			try:	
				if login == 'root':
					print('['+login+'@'+node+']'+os.pathsep+'#',end=' ')
					comm = input()
					if comm == 'exit':
						time.sleep(1)
						print('\n[!] Exited this terminal !')
						time.sleep(1)
						os.system('clear')
						break
					if comm == 'clear':
						os.system('clear')
						banner()
					else:
						print()
						subprocess.call([comm],shell=True)
						print()
				else:
					print('['+login+'@'+node+']'+os.pathsep+'$',end=' ')
					comm = input()
					if comm == 'exit':
						time.sleep(1)
						print('\n[!] Exited this terminal !')
						time.sleep(1)
						os.system('clear')
						break
					if comm == 'clear':
						os.system('clear')
						banner()
					else:
						print()
						subprocess.call([comm],shell=True)
						print()
			except FileNotFoundError:
				print('Cannot find that file !')
		except KeyboardInterrupt:
			print()
			pass
	except EOFError:
		print()
		pass	
				
					
