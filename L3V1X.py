
					
#! /usr/bin/python3

import subprocess
import time
import os

os.system('clear')
time.sleep(2)

try:
    def help():
        print('Usage:-\n\thelp - Prints this help message.')
        print('\tclear - Clears Screen Display with banner.')
        print('\tbanner - Clears Screen and prints banner and list of apps.')
        print('\t16 or exit - Exits the program.')
    def banner():
        os.system('clear')
        subprocess.call('sticks.py',shell=True)
    def lists():
        banner()
        menu = ['1. File Viewer','2. Wireless Info (wlan0)','3. Change MAC Address','4. Count file/folder','5. Open up terminal','6. Play Musics','7. Network info (eth0/wlan0)','8. PowerOff/Reboot System','9. Rock-Paper-Scissor (game)','10. Search file','11. Create File / Directory','12. Delete File / Directory','13. PDF Viewer','14. App Manager','15. Handle Processes','16. Exit Program']
        for i in menu:
            print(i)
except KeyboardInterrupt:
    print('\n[!] Found Interruption\n[!] Exiting Code !')
    pass
def caller():
    try:
        while True:
            print()
            print(os.uname()[1]+'@',end='')
            choice = input('L3V1X > ')
            if choice == '1':
                while True:
                    subprocess.call(['File_Content_Displayer.py'])
                    time.sleep(2)
                    print('\n[+] Press [R] to Run Again [M]for Menu\n')
                    select = input('[R]un Again or [M]enu: ')
                    if select == 'R' or select == 'r':
                        continue
                    elif select == 'M' or select == 'm':
                        os.system('clear')
                        lists()
                        break
                    else:
                        print('\n[+] Press [R] to Run Again [M] for Menu\n')
                        time.sleep(1)
                        print('\nGetting back to menu !\n')
                        os.system('clear')
                        lists()
                        break
            elif choice == '2':
                while True:
                    subprocess.call(['iwconfig_fetcher.py'])
                    time.sleep(2)
                    print('\n[+] Press [R] to Run Again [M]for Menu\n')
                    select = input('[R]un Again or [M]enu: ')
                    if select == 'R' or select == 'r':
                        continue
                    elif select == 'M' or select == 'm':
                        os.system('clear')
                        lists()
                        break
                    else:
                        print('\n[+] Press [R] to Run Again [M] for Menu\n')
                        time.sleep(1)
                        print('\nGetting back to menu !\n')
                        os.system('clear')
                        lists()
                        break
            elif choice == '3':
                while True:
                    subprocess.call(['Mac_Changer.py'])
                    time.sleep(2)
                    print('\n[+] Press [R] to Run Again [M]for Menu\n')
                    select = input('[R]un Again or [M]enu: ')
                    if select == 'R' or select == 'r':
                        continue
                    elif select == 'M' or select == 'm':
                        os.system('clear')
                        lists()
                        break
                    else:
                        print('\n[+] Press [R] to Run Again [M] for Menu\n')
                        time.sleep(1)
                        print('\nGetting back to menu !\n')
                        os.system('clear')
                        lists()
                        break
            elif choice == '4':
                while True:
                    subprocess.call(['file_count.py'])
                    time.sleep(2)
                    print('\n[+] Press [R] to Run Again [M]for Menu\n')
                    select = input('[R]un Again or [M]enu: ')
                    if select == 'R' or select == 'r':
                        continue
                    elif select == 'M' or select == 'm':
                        os.system('clear')
                        lists()
                        break
                    else:
                        print('\n[+] Press [R] to Run Again [M] for Menu\n')
                        time.sleep(1)
                        print('\nGetting back to menu !\n')
                        os.system('clear')
                        lists()
                        break
            elif choice == '5':
                while True:
                    subprocess.call(['L3V1ATH0N.py'])
                    time.sleep(2)
                    print('\n[+] Press [R] to Run Again [M]for Menu\n')
                    select = input('[R]un Again or [M]enu: ')
                    if select == 'R' or select == 'r':
                        continue
                    elif select == 'M' or select == 'm':
                        os.system('clear')
                        lists()
                        break
                    else:
                        print('\n[+] Press [R] to Run Again [M] for Menu\n')
                        time.sleep(1)
                        print('\nGetting back to menu !\n')
                        os.system('clear')
                        lists()
                        break
            elif choice == '6':
                while True:
                    subprocess.call(['Music_Player.py'])
                    time.sleep(2)
                    print('\n[+] Press [R] to Run Again [M]for Menu\n')
                    select = input('[R]un Again or [M]enu: ')
                    if select == 'R' or select == 'r':
                        continue
                    elif select == 'M' or select == 'm':
                        os.system('clear')
                        lists()
                        break
                    else:
                        print('\n[+] Press [R] to Run Again [M] for Menu\n')
                        time.sleep(1)
                        print('\nGetting back to menu !\n')
                        os.system('clear')
                        lists()
                        break
            elif choice == '7':
                while True:
                    subprocess.call(['ifconfig_fetcher.py'])
                    time.sleep(2)
                    print('\n[+] Press [R] to Run Again [M]for Menu\n')
                    select = input('[R]un Again or [M]enu: ')
                    if select == 'R' or select == 'r':
                        continue
                    elif select == 'M' or select == 'm':
                        os.system('clear')
                        lists()
                        break
                    else:
                        print('\n[+] Press [R] to Run Again [M] for Menu\n')
                        time.sleep(1)
                        print('\nGetting back to menu !\n')
                        os.system('clear')
                        lists()
                        break
            elif choice == '8':
                while True:
                    subprocess.call(['Power.py'])
                    time.sleep(2)
                    print('\n[+] Press [R] to Run Again [M]for Menu\n')
                    select = input('[R]un Again or [M]enu: ')
                    if select == 'R' or select == 'r':
                        continue
                    elif select == 'M' or select == 'm':
                        os.system('clear')
                        lists()
                        break
                    else:
                        print('\n[+] Press [R] to Run Again [M] for Menu\n')
                        time.sleep(1)
                        print('\nGetting back to menu !\n')
                        os.system('clear')
                        lists()
                        break
            elif choice == '9':
                while True:
                    subprocess.call(['rock-paper-scissor.py'])
                    time.sleep(2)
                    print('\n[+] Press [R] to Run Again [M]for Menu\n')
                    select = input('[R]un Again or [M]enu: ')
                    if select == 'R' or select == 'r':
                        continue
                    elif select == 'M' or select == 'm':
                        os.system('clear')
                        lists()
                        break
                    else:
                        print('\n[+] Press [R] to Run Again [M] for Menu\n')
                        time.sleep(1)
                        print('\nGetting back to menu !\n')
                        os.system('clear')
                        lists()
                        break
            elif choice == '10':
                while True:
                    subprocess.call(['findfile.py'])
                    time.sleep(2)
                    print('\n[+] Press [R] to Run Again [M]for Menu\n')
                    select = input('[R]un Again or [M]enu: ')
                    if select == 'R' or select == 'r':
                        continue
                    elif select == 'M' or select == 'm':
                        os.system('clear')
                        lists()
                        break
                    else:
                        print('\n[+] Press [R] to Run Again [M] for Menu\n')
                        time.sleep(2)
                        print('\nGetting back to menu !\n')
                        os.system('clear')
                        lists()
                        break
            elif choice == '11':
                while True:
                    subprocess.call(['Createfile.py'])
                    time.sleep(2)
                    print('\n[+] Press [R] to Run Again [M]for Menu\n')
                    select = input('[R]un Again or [M]enu: ')
                    if select == 'R' or select == 'r':
                        continue
                    elif select == 'M' or select == 'm':
                        os.system('clear')
                        lists()
                        break
                    else:
                        print('\n[+] Press [R] to Run Again [M] for Menu\n')
                        time.sleep(1)
                        print('\nGetting back to menu !\n')
                        os.system('clear')
                        lists()
                        break
            elif choice == '12':
                while True:
                    subprocess.call(['Removefile.py'])
                    time.sleep(2)
                    print('\n[+] Press [R] to Run Again [M]for Menu\n')
                    select = input('[R]un Again or [M]enu: ')
                    if select == 'R' or select == 'r':
                        continue
                    elif select == 'M' or select == 'm':
                        os.system('clear')
                        lists()
                        break
                    else:
                        print('\n[+] Press [R] to Run Again [M] for Menu\n')
                        time.sleep(1)
                        print('\nGetting back to menu !\n')
                        os.system('clear')
                        lists()
                        break
            elif choice == '13':
                while True:
                    subprocess.call(['pdf_viewer.py'])
                    time.sleep(2)
                    print('\n[+] Press [R] to Run Again [M]for Menu\n')
                    select = input('[R]un Again or [M]enu: ')
                    if select == 'R' or select == 'r':
                        continue
                    elif select == 'M' or select == 'm':
                        os.system('clear')
                        lists()
                        break
                    else:
                        print('\n[+] Press [R] to Run Again [M] for Menu\n')
                        time.sleep(1)
                        print('\nGetting back to menu !\n')
                        os.system('clear')
                        lists()
                        break
            elif choice == '14':
                while True:
                    subprocess.call(['Software_Packages.py'])
                    time.sleep(1)
                    print('\n[+] Press [R] to Run Again [M]for Menu\n')
                    select = input('[R]un Again or [M]enu: ')
                    if select == 'R' or select == 'r':
                        continue
                    elif select == 'M' or select == 'm':
                        os.system('clear')
                        lists()
                        break
                    else:
                        print('\n[+] Press [R] to Run Again [M] for Menu\n')
                        time.sleep(1)
                        print('\nGetting back to menu !\n')
                        os.system('clear')
                        lists()
                        break
            elif choice == 'banner' or choice == 'Banner':
                banner()
                time.sleep(2)
                lists()
                pass
            elif choice == 'clear':
                os.system('clear')
                continue
            elif choice == 'help':
                help()
                break
            elif choice == '15':
                while True:
                    subprocess.call('process_handler.py')
                    time.sleep(1)
                    print('\n[+] Press [R] to Run Again [M]for Menu\n')
                    select = input('[R]un Again or [M]enu: ')
                    if select == 'R' or select == 'r':
                        continue
                    elif select == 'M' or select == 'm':
                        os.system('clear')
                        lists()
                        break
                    else:
                        print('\n[+] Press [R] to Run Again [M] for Menu\n')
                        time.sleep(1)
                        print('\nGetting back to menu !\n')
                        os.system('clear')
                        lists()
                        break
            elif choice == '16' or choice == 'exit':
                print('\n[!] Exiting Code !')
                time.sleep(1)
                print('\n[+] Clearing Cache !')
                time.sleep(1)
                print('\n[!] Exited Successfully !')
                time.sleep(1)
                os.system('clear')
                break
            else:
                help()
                print()
                continue
    except KeyboardInterrupt:
        print('\n[!] Found Interruption\n[!] Exiting Code !')
        pass
try:
    banner()
    lists()
    caller()
except FileNotFoundError:
    print('\n\tUnable to find some packages. Please verify code and packages !')
