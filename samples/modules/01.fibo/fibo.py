
def fibo(n):
    if n == 0:
        return 0

    curr, prev = 1, 0

    for i in range(1, n):
        curr, prev = curr + prev, curr

    return curr

