from bs4 import BeautifulSoup
import requests
x = 1
y = 120
while x <= 10:
	url = "https://jacksonville.craigslist.org/search/cta?s=" + str(y) 
	source = requests.get(url)
	text_data = source.text 
	soup = BeautifulSoup(text_data)
	for title in soup.find_all(class_="result-title hdrlnk"):
		print (title.text)
	x += 1
	y += 120