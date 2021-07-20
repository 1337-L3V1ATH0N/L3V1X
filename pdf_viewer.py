#! /usr/bin/python3

import os
import time
import subprocess

os.system('clear')

try:
	print('\n\t\t\t\t[ PDF Viewer ]\n')

	path = input('\n[*] Enter your path to PDF : ')

	time.sleep(1)
	os.chdir(path)
	print('\n[+] Changed to',os.getcwd())
	time.sleep(1)
	print('\nFound Those PDF files in',os.getcwd())
	time.sleep(1)
	print()
	for doc in os.listdir(path):
		if '.pdf' in doc:		
			print(doc)
	
	pdf = input('\n[*] Enter PDF name to view : ')
	
	print('Please Wait...')
	
	time.sleep(2)
	
	subprocess.call(['evince',pdf])

except FileNotFoundError:
	print('\nMaybe you don\'t have required tools installed !')
	time.sleep(1)
	print('Installing Required Tools...')
	time.sleep(2)
	subprocess.call(['sudo','apt-get','install','evince'])
	time.sleep(2)
	print('Insalled tools successfully ')
	time.sleep(1)
	print('Now run again program ')
	
