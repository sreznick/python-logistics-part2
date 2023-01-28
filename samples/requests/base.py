import requests

response = requests.get('https://docs.python.org/3/library/index.html')

print(response.text)

