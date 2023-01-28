import requests

response = requests.get('https://www.python.org/ftp/python/3.11.1/Python-3.11.1.tar.xz', stream=True)

STEP = 1024 * 1024

with open('Python-3.11.1.tar.xz', 'wb') as f:
    total = 0
    for data in response.iter_content(1024):
        prev_total = total
        total += len(data)
        f.write(data)

        prev_steps = prev_total // STEP
        steps = total // STEP

        for _ in range(steps - prev_steps):
            print('#', end='', flush=True)
            

print()

