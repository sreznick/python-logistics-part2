import requests

response = requests.get('https://docs.python.org/3/library/index.html')
for key, value in response.headers.items():
    print("header key", key)
    print("header value", value)
    print()


