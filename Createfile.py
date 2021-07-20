#! /usr/bin/python3

import os
import time
import subprocess
try:
    def help():
        print('Usage:-\n\t1 - Creates Files on given path.')
        print('\t2 - Creates Folders on given path.')
        print('\thelp - Prints this message.')
        print('\texit - Exits this program.')
        print('\tclear - Clears the screen.')

    os.system('clear')
    while True:
        print('\n\t\t\t===== [ Creator ] =====\n')

        create = ['1. Create File','2. Create Folder']

        for i in create:
	        print(i)
        choice = input('\n[*] Enter creation : ')
        if choice == '1':
	        print('\n[*] Current Path',os.getcwd())
	        time.sleep(2)
	        path = input('\n[*] Where to create file ? Enter Path : ')
	        os.chdir(path)
	        print('\n[*] Changed to ',os.getcwd())
	        file = input('\n[*] Enter your filename with extension :')
	        subprocess.call(['touch',file])
	        time.sleep(1)
	        print('\nFile Created')
        elif choice == '2':
	        print('\n[*] Current Path',os.getcwd())
	        time.sleep(2)
	        path = input('\n[*] Where to create folder ? Enter Path : ')
	        os.chdir(path)
	        print('\n[*] Changed to',os.getcwd())
	        folder = input('\n[*] Enter your folder name : ')
	        subprocess.call(['mkdir',folder])
	        time.sleep(1)
	        print('\nFolder Created')
        elif choice == 'help':
            help()
            break
        elif choice == 'clear':
            os.system('clear')
            continue
        elif choice == 'exit':
            exit(0)
        else:
            print('\n[!] Unable to understand input...\nExiting')
            break
except:
    print('\n[!] Encountered Errors... Exiting... ')
    pass
