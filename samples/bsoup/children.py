import requests
from bs4 import BeautifulSoup

response = requests.get('https://docs.python.org/3/library/index.html')
soup = BeautifulSoup(response.text, 'html.parser')
for e in soup.body.children:
    print(e.name)

