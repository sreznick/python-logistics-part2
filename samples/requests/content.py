import requests

response = requests.get('https://docs.python.org/3/library/index.html')
print("content")
print("type", type(response.content))
print(response.content[:100])

print()
print('-----------------------')
print()

print("text")
print("type", type(response.text))
print(response.text[:100])
print()

