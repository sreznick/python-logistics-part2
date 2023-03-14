import requests
import json

response = requests.get('https://www.reddit.com/r/Python/.json')
data = json.loads(response.text)

print(data)

