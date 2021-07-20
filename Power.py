#! /usr/bin/python3

import os
import time

print('\n\t\t\t\t[ Over-Powered ]\t\t\n')

menu = ['1. Power Off\n','2. Reboot\n']

for menus in menu:
	print(menus)

print('\n[*] Select your Power : ',end='')

power = input()

if power == '1':
	
	print('[!] Senorita !!! you have chosen DEATH !')
	time.sleep(1)
	print('[!] I Will KILL your SYSTEM ! in 10 seconds HAHA... ! ')
	time.sleep(6)
	print('\n[!] Pray For Mercy !')
	time.sleep(4)
	os.system('poweroff')
elif power == '2':
	print('[!] Senorita !!! you have chosen Re-Birth !')
	time.sleep(1)
	print('[!] I am Killing your SYSTEM for your new birth ! in 10 seconds HAHA... ! Die You Scum')
	time.sleep(6)
	print('\n[!] Peace was never an Option !')
	time.sleep(4)
	os.system('reboot')
else:
	print('[!] You Scum you injured me whith those Wrong Inputs !!!! Any ways i am killing you in 10 seconds !')
	time.sleep(10)
	os.system('poweroff') 
