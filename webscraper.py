import requests
from bs4 import BeautifulSoup

url = ""
full_page = requests.get(url)
text = full_page.text
soup = BeautifulSoup(text)
print (soup)
