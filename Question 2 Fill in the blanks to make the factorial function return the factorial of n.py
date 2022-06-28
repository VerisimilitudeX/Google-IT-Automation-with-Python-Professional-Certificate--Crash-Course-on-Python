def factorial(n):
    if n == 0:
        return 1
    result = n
    for x in range(1, n):
        result *= x
    return result

for n in range(0, 10):
    print(n, factorial(n))
