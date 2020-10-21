import os
import sys
import time
import requests
from bs4 import BeautifulSoup

def clear(): os.system('clear');
def printRed(skk): print("\033[91m{}\033[00m" .format(skk))
def printGreen(skk): print("\033[92m{}\033[00m" .format(skk))
def printYellow(skk): print("\033[93m{}\033[00m" .format(skk))
def create_space(player_name): return ' '*(MAX_LEN-len(player_name))


MAX_LEN=21

#input
world = "Elysia"
if(len(sys.argv)>1):
	world = sys.argv[1]

printYellow(f'Retrocores Online - {world}')

while(True):
	soup = BeautifulSoup(requests.get(f'https://mastercores.com/?subtopic=community&view=online&world={world}&sort=level').text,'lxml')
	time.sleep(16)
	dataServer = soup.find('table',id="WorldOverViewMaxOnline").text.splitlines()
	dataPlayer = soup.find('table',id="WorldOverViewList").find_all('tr')

	clear()
	# SERVER INFO
	#for x in dataServer: printYellow(x)
	printGreen(dataServer[1])
	print(dataServer[2])

	printGreen("player online")
	# PLAYER ONLINE
	for x in dataPlayer:
		player_data = x.find_all('td')
		print(f"{player_data[0].text} {create_space(player_data[0].text)} {player_data[1].text.rjust(5, ' ')} {player_data[2].text}")


