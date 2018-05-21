import requests
from bs4 import BeautifulSoup


x = 1
while x < 20:
	url = "http://redditlist.com/?page=" + str(x)
	alldata = requests.get(url)
	text = alldata.text
	soup = BeautifulSoup(text, "html.parser")
	for titles in soup.find_all(class_="sfw"):
		f = open("namelist.txt", "a")
		f.write(titles.text)
		f.close()
	x += 1
