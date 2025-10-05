def fatorial(n):
    if n < 0:
        return None
    elif n <= 1:
        return 1
    return n * fatorial(n - 1)

print(fatorial(3))
print(fatorial(4))
print(fatorial(6))

print(fatorial(-2))
print(fatorial(1))
print(fatorial(0))