from bs4 import BeautifulSoup
import requests
x = 1
y = 120
while x <= 10:   #loops through more than one page
	url = "https://jacksonville.craigslist.org/search/boo?s=" + str(y) #adds new pages to url 
	source = requests.get(url) #pulls html
	text_data = source.text  # readable formate
	soup = BeautifulSoup(text_data, "html.parser") # BS OBJECT
	for title in soup.find_all(class_="result-title hdrlnk"): # using soup object to find titles in html class
		f = open("namelist.txt","a") # create new file
		f.write(title.text) # put titles on hard drive in text format
		f.close() 
	x += 1
	y += 120