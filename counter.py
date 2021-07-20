#! /usr/bin/python3

import os
import time
import subprocess

try:
    def help():
        print('\nUsage :-\n\tS / s\t\t\tset path to other directory. eg :- /home/$USER/Downloads to access Downloads directory.')
        print('\tC / c\t\t\tset path to current directory.')
        print('\thelp / h\t\tprint this help message.')
        print('\texit / [Ctrl+c]\t\tExit Forcefully !\n')
    
    loop=1
    print('\n\t\t-=-=-=-= Counter Directory =-=-=-=-')
    print('\n\n[NOTE] For Instructions type \'help\'.')
    print('\n[+] Current Path',os.getcwd())

    choice = input('\n[S]et Path [C]urrent Path : ')

    if choice == 'C' or choice == 'c':
	    print('[+] Selecting current path',os.getcwd())
	    for i in os.listdir(os.getcwd()):
	    	print(loop,i)
	    	loop+=1
    
    elif choice == 'S' or choice == 's':
	    path = input('Path to move : ')
	    print('\n[...] Changing to Path',path)
	    time.sleep(1)
	    os.chdir(path)
	    for i in os.listdir(path):
	    	print(loop,i)
	    	loop+=1
    elif choice == 'help' or choice == 'h':
        help()
    elif choice == 'exit' or choice == 'Exit':
        exit(0)
    else:
        print('\n[ERROR] Unable to fetch data. Please check you are providing correct commands !')
        help()
except:
    if KeyboardInterrupt:
        print('\n[+] Exited by USER.')
        pass
    else:
        print('\n[ERROR] Encountered Error !')
        print('\n[!] Exiting ')
        exit(1)
