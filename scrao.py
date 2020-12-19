from bs4 import BeautifulSoup
import requests
import os
import sys
import time
#AUTHOR : VeeX/NAoHR/Najmi
os.system("clear")
sys.stdout.write(
"""
Welcome to lyrics scrapper

all the lyrics are from 
"search.azlyrics.com"
hope u enjoy this program :)
Usage: <song> <artist>
	wh/<>
Author:VeeX


""")
try:
	i = 1
	stop = False
	while(not stop):
		i +=1
		inputan = str(input("song : "))
		if inputan == "quit":
			stop = True
		elif inputan == "clear":
			os.system("clear")
		else:
			plus = inputan.replace(' ','+')
			print('searching for',inputan)
			page = requests.get('https://search.azlyrics.com/search.php?q='+plus)
			soup = BeautifulSoup(page.content,'html.parser')
			pemisahan = soup.find(class_='table table-condensed')
			try:
				link = pemisahan.find_all('td',class_='text-left visitedlyr')
			except AttributeError as e:
				print("try another song")
			kumpulan = []
			j = 0
			for item in link:
				j +=1
				if j <= 6:
					print(item.text)
					kumpulan.append(item)
				else:
					pass
			try:
				song_u_want = int(input("number : "))
			except ValueError:
				print("value must be an integer")
			seperate = kumpulan[song_u_want-1]
			print("Searching for : ",seperate.text)
			seperate1 = [item for item in seperate]
			close = str(seperate1[1])
			go_to = close[close.find('//')+2:close.find('>')-1]
			final = "https://"+go_to
			print("searching for lyrics....")
			print("lyrics : ")
			page = requests.get(final)
			soup = BeautifulSoup(page.content,'html.parser')
			lyrics = soup.find('div',attrs={'class':None,'id':None})
			try:
				print(lyrics.text)
			except AttributeError:
				print("this is an album try something new like 'song' 'the artist'")
				import scrao
except requests.exceptions.ConnectionError:
	print("=====================================")
	print("please check your internet Connection")
	print("=====================================")
except IndexError:
	a ="u chose nothing"
	b = "you pressed some thing while this program search something"
	c = "or perhaps"
	print(" "*(len(b)-len(a))+a)
	print(" "*(len(b)-len(c))+c)
	print(b)
	import scrao
except KeyboardInterrupt:
	print("\nQUIT")
except NameError:
	print("try another song")
	a = "...."
	for i in a:
		sys.stdout.write(i)
		time.sleep(0.1)
	import scrao
