#! /usr/bin/python3

import subprocess
import time
import os

os.system('clear')

try:

	print('\n\t\t\t\t\t ==-==-[ Software Manager ]-==-==\n')

	action = ['1. Install Software','2. Remove Software','3. Search Software Database']
	for a in action:
		print(a)
	choice = input('\n[*] Action >>> ')
# Installs software from repositories
	if choice == '1':
		inst_app = input('\n[*] Enter name of app to install :')
		app = subprocess.check_output('sudo apt-get install '+inst_app,shell=True,text=True).split('\n')
		for a in app:
			if inst_app+' is already' in a:
				print(a)
				break
		else:
			print('\n[+] Installed {} Successfully '.format(inst_app))
# Removes app with and without configuration files
	elif choice == '2':
		rem_what = ['\n\t[i] Inlcude Configuration files','\t[e] Exclude Configuration files.']
		for r in rem_what:
			print(r) 
		choice = input('\n[*] Remove with >>> ')
	# Removes apps with configuration files
		if choice == 'i' or choice == 'I':
			rem_app = input('[*] Enter name app to remove with configuration file : ')
			print('\t\t Press Y to Continue N to Cancel ( [NB] Not required when no app found : )')
			app = subprocess.check_output('sudo apt-get purge '+rem_app,shell=True,text=True).split('\n')
			for p in app:
				if 'Package \''+rem_app+'\' is not installed' in p:
					print(p)
					break
			else:			
				print('\n[+] Removed {} with Configuration files Successfully'.format(rem_app))
							
					
	# Removes apps without configuration files
		elif choice == 'e' or choice == 'E':
			rem_app = input('[*] Enter name app to remove without configuration file : ')
			print('\t\t Press Y to Continue N to Cancel ( [NB] Not required when no app found : )')
			app = subprocess.check_output(['sudo apt-get remove '+rem_app],shell=True,text=True).split('\n')
			for p in app:
				if 'Package \''+rem_app+'\' is not installed' in p:
					print(p)
					break
			else:			
				print('\n[+] Removed {} without Configuration files Successfully'.format(rem_app))
		else:	
			print('\n{!} Exiting program !')
# Searches Database to check whether app is already installed or not !
	elif choice == '3':
		sear_app = input('\n[*] Search App >>> ')
		app = subprocess.check_output('sudo apt-cache search '+sear_app,shell=True,text=True).split('\n')
		for ap in app:
			print(ap)
	else:
		print('Invalid Input ! Quiting...')
		pass
		
				
except :
	pass
