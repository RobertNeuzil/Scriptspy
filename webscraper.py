import requests
from bs4 import BeautifulSoup

url = "https://jacksonville.craigslist.org/d/housing-swap/search/swp"
all_data = requests.get(url)
text_format = all_data.text
#print (text_format)
soup = BeautifulSoup(text_format)
#print (soup)

for links in soup:
	final = soup.find_all("a", {"class=", "result-title hdrlnk"})
	print (final)
