#! /usr/bin/python3

import subprocess
import os 
import time
try:
    os.system('clear')
    name = os.uname()[1]
    time.sleep(1)
    def help():
        print('Usage:- \n\tclear - Clears the screen.')
        print('\texit - Exits the program.')
        print('\thelp - Prints this message.')
        print('\t1 - Set the resources for you program to run.')
        print('\t2 - Reset the resources of your running program.')
        print('\tuse or USE - Prints the message for questions like why we need this program !')
       
        
    print('\n\t\t\t\t[ Process Handler ]\n')
    while True:
        print('\n[ NB ] For Instructions type \'help\'\n')
        prcs = ['1. Set Process rate','2. Reset Process rate']
        for prc in prcs:
            print(prc)
        choice = input('\n[*] Handle processes on your finger tip : ')
        if choice == 'USE' or choice == 'use' or choice == 'Use':
            os.system('clear')
            print('\n\n\tProcess Handler helps you to increase or decrease the priority of a process. This tool will make software workings fast or slow, according to your needs. This tool will never work for root user.\n')
            time.sleep(5)
        elif choice == '1':
            process = input('[*] Enter the name of tool you want to run with selected priority : ')
            prior = input('\n\t\t[ALERT] Select level of process [v]ery-Low, [L/l]ow, [D/d]efault, [H]igh, [V]ery-High : ')
            if prior == 'v':
                subprocess.call('nice -n +19 '+process,shell=True)
                print('\n \tPriority of {} set to [VERY LOW] !\n'.format(process))
            elif prior == 'L' or prior == 'l':
                subprocess.call('nice -n +10 '+process,shell=True)
                print('\n \tPriority of {} set to [LOW] !\n'.format(process))
            elif prior == 'D' or prior == 'd':
                subprocess.call('nice -n +0 '+process,shell=True)
                print('\n \tPriority of {} set to [DEFAULT] !\n'.format(process))
            elif prior == 'H' or prior == 'h':
                subprocess.call('nice -n -10 '+process,shell=True)
                print('\n \tPriority of {} set to [HIGH] !\n'.format(process))
            elif prior == 'V':
                subprocess.call('nice -n -19 '+process,shell=True)
                print('\n \tPriority of {} set to [VERY HIGH] !\n'.format(process))
            else:
                print('\n\t\t[ERROR] Wrong level of priority by pressing [',prior,']')
                break
        elif choice == '2':
            values = subprocess.check_output(['ps','aux']).decode('utf-8').split('\n')
            for value in values:
                if 'USER' in value: # Checks the string user in ps aux output if yes then prints USER PID COMMAND
                    ps_title = value.split(' ')[0:]
                    print(ps_title[0],'\t',ps_title[-22],'\t',ps_title[-1]) # Prints USER PID COMMAND
                if name.lower()[0:5] in value: # Username in lower case only for non-root user
                    ps_pid = value.split(' ')
                    print(ps_pid[0],ps_pid[4],ps_pid[-1]) # Prints USER NAME, PROCESS ID, PRINTS PROCESS COMMAND
            pid = input('\n\t[*] Enter PID of process you want to reset : ')
            time.sleep(1)
            prior = input('\n\t\t[ALERT] Select level of process [v]ery-Low, [L/l]ow, [D/d]efault, [H]igh, [V]ery-High : ')
            if prior == 'v':
                subprocess.call('renice +19 '+pid,shell=True)
                print('\n \t[RESET] Priority of {} reset to [VERY LOW] !\n'.format(pid))
            elif prior == 'L' or prior == 'l':
                subprocess.call('renice +10 '+pid,shell=True)
                print('\n \t[RESET] Priority of {} reset to [LOW] !\n'.format(pid))
            elif prior == 'D' or prior == 'd':
                subprocess.call('renice 0 '+pid,shell=True)
                print('\n \t[RESET] Priority of {} reset to [DEFAULT] !\n'.format(pid))
            elif prior == 'H' or prior == 'h':
                subprocess.call('renice -10 '+pid,shell=True)
                print('\n \t[RESET] Priority of {} reset to [HIGH] !\n'.format(pid))
            elif prior == 'V':
                subprocess.call('renice -19 '+pid,shell=True)
                print('\n \t[RESET] Priority of {} reset to [VERY HIGH] !\n'.format(pid))
            else:
                print('\n\t\t[ERROR] Wrong level of priority by pressing [',prior,']')
                break
            continue
        elif choice == 'help':
            help()
            break
        elif choice == 'clear':
            os.system('clear')
            continue
        elif choice == 'exit':
            print('\n[*] Exited Code !')
            exit(0)
        else:
            print('\n[!] Cannot run tool using {} input...'.format(choice))
except KeyboardInterrupt:
	#print('\n[!] Exited Code !')
	#time.sleep(1)
	#os.system('clear')
    print('\n[*] Exited Code !')
    time.sleep(2)
    os.system('clear')
    pass
