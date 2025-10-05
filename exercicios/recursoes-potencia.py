def potencia(base, expoente):
    if expoente < 0:
        return None
    elif expoente == 0:
        return 1
    return base * potencia(base, expoente - 1)

print(2 ** 5)
print(potencia(2, 5))

print(10 ** 1)
print(potencia(10, 1))

print(10 ** -1)
print(potencia(10, -1))

print(10 ** 0)
print(potencia(10, 0))