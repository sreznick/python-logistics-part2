import requests

response = requests.get('https://google.com', params={'q': 'Python'})
print(response.status_code)

