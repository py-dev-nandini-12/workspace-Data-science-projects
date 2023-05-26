def fib(n):
    if n < 0:
        return None
    if n < 3:
        return 1

    return fib(n-1) + fib(n-2)  # recusrive method


for n in range(1, 8):
    print(n, ':', fib(n))
