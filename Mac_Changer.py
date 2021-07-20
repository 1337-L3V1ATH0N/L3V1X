
#! /usr/bin/python3

import subprocess 
import time
import os


os.system('clear')

print('\n\t\t\t===== Mac Changer =====\n')
interfaces = ['1. ifconfig eth0','2. ifconfig wlan0']

for i in interfaces:
	print(i)

inp_inter = input('\n[*] Enter your interface : ')
time.sleep(1)

if inp_inter == '1':
	print('\n[+] Selected interface ifconfig eth0')
	time.sleep(1)
	choice = input('\n[*] Do you want to use default mac ? [y] for yes [n] for no : ')
	if choice == 'n':
		print('\n[*] Enter your chosen MAC ADDRESS ')
		mac_addr = input('>>> ')
		time.sleep(2)		
		subprocess.call(['sudo','ifconfig','eth0','down'])
		subprocess.call(['sudo','ifconfig','eth0','hw','ether',mac_addr])
		subprocess.call(['sudo','ifconfig','eth0','up'])
		print('\n[+] Changing Mac Address of LAN')
		time.sleep(2)
		print('\n[+] Changed Mac to',mac_addr)
	if choice == 'y':
		time.sleep(2)
		subprocess.call(['sudo','ifconfig','eth0','down'])
		subprocess.call(['sudo','ifconfig','eth0','hw','ether','00:11:22:33:45:56'])
		subprocess.call(['sudo','ifconfig','eth0','up'])
if inp_inter == '2':
	time.sleep(1)
	choice = input('\n[*] Do you want to use default mac ? [y] for yes [n] for no : ')
	if choice == 'n':
		print('\n[*] Enter your chosen MAC ADDRESS ')
		mac_addr = input('>>> ')
		time.sleep(2)		
		subprocess.call(['sudo','ifconfig','wlan0','down'])
		subprocess.call(['sudo','ifconfig','wlan0','hw','ether',mac_addr])
		subprocess.call(['sudo','ifconfig','wlan0','up'])
		print('\n[+] Changing Mac Address of LAN')
		time.sleep(2)
		print('\n[+] Changed Mac to',mac_addr)
	if choice == 'y':
		time.sleep(2)
		subprocess.call(['sudo','ifconfig','wlan0','down'])
		subprocess.call(['sudo','ifconfig','wlan0','hw','ether','00:11:22:33:45:56'])
		subprocess.call(['sudo','ifconfig','wlan0','up'])
elif inp_inter != '1' and inp_inter != '2':
	print('\n[!] Invalid Option !')
