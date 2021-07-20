#! /usr/bin/python3

import os
import time
#import subprocess

os.system('clear')
time.sleep(2)
try:
    def help():
        print('Usage:-\n\tY or y - Sets New Path to access.')
        print('\tN or n - Sets current directory as path.')
        print('\thelp - Prints this message.')
        print('\texit - Exits Program')
        print('\tclear - Clears the screen')
    
    while True:
        print('\n\t\t\t\t[ File Content Displayer ]\t\n')

        print('[+] Current Path : ',os.getcwd())
        time.sleep(1)

        choice = input('\n[Y] to set new path [N] to set directory as current path : ')
        if choice == 'y' or choice == 'Y':
            path = input('\n[*] Enter your path : ')
            os.chdir(path)
            time.sleep(1)
            print('\n[+] Path changed to',os.getcwd())
            time.sleep(1)
            for file_name in os.listdir(path):
                if '.txt' in file_name:
                    print()
                    print('[T] Text File:',file_name)
                else:
                    print('[O] Other File:',file_name)
            file = input('\n[*] Enter your filename with extension : ')
            os.system('cat '+file)
        elif choice == 'n' or choice == 'N':
            print('\n[+] You are in current directory',os.getcwd())
            for file_name in os.listdir(os.getcwd()):
                if '.txt' in file_name:
                    print()
                    print('[T] Text File:',file_name)
                else:
                    print('[O] Other File:',file_name)
            file = input('\n[*] Enter your filename with extension : ')
            os.system('cat '+file)
        elif choice == 'help':
            help()
            break
        elif choice == 'clear':
            os.system('clear')
            continue
        elif choice == 'exit':
            exit(0)
        else:
            help()
            break
except KeyboardInterrupt:
    print('\n[!] User Exited')
