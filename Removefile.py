#! /usr/bin/python3

import os
import time
import subprocess

os.system('clear')
print('\n\t\t\t===== [ Destructor ] =====\n')

create = ['1. Delete File','2. Delete Folder']

for i in create:
	print(i)

choice = input('\n[*] Enter Destruction : ')

if choice == '1':
	print('\n[*] Current Path',os.getcwd())
	time.sleep(2)
	path = input('\n[*] Where to delete file ? Enter Path : ')
	os.chdir(path)
	print('\n[*] Changed to ',os.getcwd())
	file = input('\n[*] Enter your filename with extension :')
	subprocess.call(['rm',file])
	time.sleep(1)
	print('\nFile Deleted')
elif choice == '2':
	print('\n[*] Current Path',os.getcwd())
	time.sleep(2)
	path = input('\n[*] Where to delete folder ? Enter Path : ')
	os.chdir(path)
	print('\n[*] Changed to',os.getcwd())
	folder = input('\n[*] Enter your folder name : ')
	subprocess.call(['rmdir',folder])
	time.sleep(1)
	print('\nFolder Deleted')
elif choice != '1' or choice != '2':
	print('\n[!] Invalid Operation Requested !')
	
