import requests
from bs4 import BeautifulSoup

site = requests.get(
"https://www.yellowpages.com/search?search_terms=burger&geo_location_terms=Jacksonville%2C+FL")
soup = BeautifulSoup(site.text, 'html.parser')
for x in soup.find_all(class_="business-name"):
	justname = x.text
	print (justname)
