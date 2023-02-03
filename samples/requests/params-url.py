import requests

response = requests.get('https://python.org',
                        params={'key': ['value1', 'value2']})
print(response.url)

response = requests.get('https://python.org',
                        params={'key': ['value1', 'value2'],
                                'key2': 'value'})
print(response.url)

