#! /usr/bin/python3

import os
import time
import random

os.system('clear')

banner = '''|---------------------------------------------|
|\t\tRock-Paper-Scissor\t      |
|---------------------------------------------|'''
print(banner)

player = 0			# 1st player point count
computer = 0	   # computer point count
draw = 0           # Counts draw between game

game = ['rock','paper','scissor','paper','scissor','rock','scissor','rock','paper']

# choice to play with !

player_limit = ['\n1] Player and Computer\n'] 

loop = 1

# Printing player_limit

for playing_choice in player_limit: 
	print(playing_choice)	

player_choice = input('\n[*] Select your Opponent : ')

if player_choice == '1':
	player_name_1 = input('\n[*] Enter your name : ')
	while loop != 10:
		time.sleep(2)
		os.system('clear')
		print(banner,end='\n\n')
		print('[+]',player_name_1+'\'s Turn : ',end='')
		play_choice = input()
		time.sleep(1)
		print('\n[+] Computer\'s Turn : ',end='')
		comp_choice = random.choice(game)
		print(comp_choice)

		try:
# Matching values of player and computer in a way when they are equal.
			if ord(play_choice[0]) ==  ord(comp_choice[0]):
				print('\n[!] It\'s a Draw.\n')
				print('['+player_name_1+'\'s Score] :',player)
				print('[Computer\'s Score] :',computer)
				draw += 1
				time.sleep(1)
			
			elif play_choice == 'scissor' and comp_choice == 'paper':
				print('\n[+]',player_name_1,'got 1 point !')
				player += 1
				print('\n['+player_name_1+'\'s Score] :',player)
				print('[Computer\'s Score] :',computer)
				time.sleep(3)

			elif play_choice == 'paper' and comp_choice == 'scissor':
				print('\n[-] Computer got 1 point !')
				computer += 1
				print('\n['+player_name_1+'\'s Score] :',player)
				print('[Computer\'s Score] :',computer)
				time.sleep(3)
# if rock is < than scissor rock wins ! if paper is < than rock paper wins !
			elif ord(play_choice[0]) < ord(comp_choice[0]): 
				print('\n[+]',player_name_1,'got 1 point !')
				player += 1
				print('\n['+player_name_1+'\'s Score] :',player)
				print('[Computer\'s Score] :',computer)
				time.sleep(3)

# if comp choice paper is < than play choice rock than paper wins !
			
			elif ord(comp_choice[0]) < ord(play_choice[0]):
				print('\n[-] Computer got 1 point !')
				computer += 1
				print('\n['+player_name_1+'\'s Score] :',player)
				print('[Computer\'s Score] :',computer)
				time.sleep(3)

		except IndexError:
			print('\n[?] Your turn cannot be empty !\n[ :( ] Ooooops !! you lost 1 point !')
			player -= 1
			print('\n['+player_name_1+'\'s Score] :',player)
			print('[Computer\'s Score] :',computer)
			time.sleep(3)		
		loop += 1
print('\n',player_name_1,' | '+'Computer')
print("-------------------\n"+"| "+str(player),"\t|\t"+str(computer),"|")

if player > computer:
	player_wins = player - computer
	print('\n[ Hurray ]',player_name_1,'win\'s with',player_wins,'points !\n')
elif computer > player:
	computer_wins = computer - player
	print('\n[ Oops ] Computer win\'s with',computer_wins,'points !\n')
else:
	print('\n[ Oh No ] It\'s a Tie... No one wins !\n')

