from bs4 import BeautifulSoup
import requests

url = "https://www.bing.com"
soup = BeautifulSoup(requests.get(url).text, 'lxml')

print(soup.prettify())
