import requests

response = requests.get('https://www.python.org/ftp/python/3.11.1/Python-3.11.1.tar.xz')
with open('Python-3.11.1.tar.xz', 'wb') as f:
    f.write(response.content)

