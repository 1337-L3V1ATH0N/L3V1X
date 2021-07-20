#! /usr/bin/python3

import subprocess
import time
import os

def help():
    print('Usage:-\n\texit - Exits Program.')
    print('\thelp - Prints this message.')
    print('\tclear - Clears Screen Display.')
    print('\tposs (Part Of Special Searching) - Prints the file related to your input. This is helpful when you don\'t know the file name correctly for a search.\n')

os.system('clear')
while True:
    try:
        print('\n\t\t\t\t=-=-=-[ File Locater ]-=-=-=\n\n')


        file = input('\n[*] Enter file name to search : ')
        if file == 'help':
            help()
            break
        elif file == 'exit':
            print('\n[!] Exited !')
            exit(0)
        elif file == 'poss':
            poss = input('\n[POSS] Enter the broken name of your search: ')
            subprocess.call(['apropos '+poss],shell=True)
        else:
            subprocess.call(['locate',file],shell=False)
            break
    except KeyboardInterrupt:
        print('\n[!] User Exited !')
