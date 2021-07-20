#! /usr/bin/python3

import subprocess
import os
import time

file = 0
dire = 0

os.system('clear')
print('\n\t\t-----| Count Files and Folders in a Folder |-----\n')
time.sleep(3)
try:
    def help():
        print('Usage:-\n\tUse or use - Why we need this program! This Prints the use.')
        print('\texit - Exits program.')
        print('\thelp - Prints this message.')

    while True:
        path = input('\n[*] Enter your path : ')
        if path == 'help':
            help()
            break
        elif path == 'exit':
            print('\n[!] Exited!')
            exit(0)
        elif path == 'use' or path == 'Use':
            print('\n[USE] This program is useful for bigger folders where we want to scan all files and folders separately and how much files and folers we have within it.')
        else:
	        print('\n[!] Changing directory to',path)
	        os.chdir(path)
	        time.sleep(1)
	        print('\n[+] Changed to',os.getcwd())
	
	        files = subprocess.check_output(['ls','-l']).decode('utf-8').split('\n')
	
	        for value in files:
		        if '-rw' in value:
			        value.split(' ')[0][8]
			        file += 1
		        elif 'drwx' in value:
			        value.split(' ')[0][8]
			        dire += 1
	        print('\n[ File ] {} = {}'.format(os.getcwd(),file))
	        print('\n[ Dir ] {} = {}'.format(os.getcwd(),dire))
except FileNotFoundError:
	print('\n[ERROR] Path or File Don\'t Exist !\n')
	pass
