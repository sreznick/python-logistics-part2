from bs4 import BeautifulSoup
import requests

response = requests.get('https://docs.python.org/3/library/index.html')
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.body.prettify())
