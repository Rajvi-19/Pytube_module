from googlesearch import search
from urllib.parse import *
import webbrowser
from pytube import YouTube as yt
import os 
#for findimg songs on youtube
def Song_finder(enter):	
	for i in search("song"+enter,stop=5):
		c=urlparse(i)
		if  c.netloc=="www.youtube.com":
			a=urlunparse(c)
			webbrowser.open(a)
			break

#for downloading songs
def Song_downloader(url):	
	for i in search("song"+url,stop=5):
		c=urlparse(i)
		if  c.netloc=="www.youtube.com":
			a=urlunparse(c)
			break
	link=yt(a)
	res=link.streams.get_highest_resolution()
	os.system('cls')#cls-for pcs clear-for phones
	print('Wait..',end='\r')
	res.download()
	print('Downloaded Successfully...')			
		

name=input("Enter Song Name: ")
#Song_finder(name)
#Song_downloader(name)