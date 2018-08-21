import requests
from bs4 import BeautifulSoup

site = requests.get(
''' enter url here '''
)
soup = BeautifulSoup(site.text, 'html.parser')
for x in soup.find_all( ["a", "title"] ):
	
	print (x.text)
