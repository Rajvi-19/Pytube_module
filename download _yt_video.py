from pytube import YouTube as yt
#Func to download youtube video
def Download(url):
	try:
		link=yt(url)
		res=link.streams.get_highest_resolution()
		res.download()
	except Exception as e:
		print(f'Error:{e}')
	else:
		print('Successfully Downloaded...')
#Calling the Func	
link=input('Enter the Link: ')
Download(link)