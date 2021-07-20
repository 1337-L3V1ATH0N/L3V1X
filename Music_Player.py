#! /usr/bin/python3

import subprocess 
import time
import os

os.system('clear')

print('\n\t\t\t\t=-=-= Music $ Player =-=-=\n')

print('\n[NB]\n\tDefault Songs will be played from Music Folder\n\tYou can change the path by entering the path to the Music file\n')

choice = input('[Y] for Default Music Folder [N] to set the path : ')
try:
	try:
		if choice == 'y' or choice == 'Y':
			time.sleep(1)
			print('\n[*] Selected default music folder')
			os.chdir('/home/'+os.getlogin()+'/Music')
			time.sleep(2)	
			#play_ms = subprocess.call(['play','*.mp3'])
			subprocess.check_output(['play','*.mp3'])
		elif choice == 'n' or choice == 'N':
			time.sleep(1)
			path = input('\n[*] Enter path to music file : ')
			time.sleep(1)
			os.chdir(path)
			print('[+] Changed path to',os.getcwd())
			time.sleep(1)
			subprocess.check_output(['play','*.mp3'])
		else:
			print('\n[!] Wrong Input... Operation Aborted !\n')
	except FileNotFoundError:
		time.sleep(3)
		print('\n[ERROR] It seems you don\'t have required tools ! Trying to install it.\n')
		subprocess.call(['sudo','apt-get','install','sox'])
		subprocess.call(['sudo','apt-get','install','sox','libsox-fmt-all'])
		time.sleep(2)
		print('\n\n\t[SUCCESS] Try to run program AGAIN !\n\n')
except:
	print('\n\n[ERROR] Encountered Error ! Exiting Code !\n')
	time.sleep(1)
	pass
