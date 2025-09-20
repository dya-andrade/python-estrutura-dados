import time

def em_segundos(funcao, *args, **kwargs):
    inicio = time.perf_counter()
    funcao(*args, **kwargs)
    fim = time.perf_counter()
    print(f"Tempo: {fim - inicio:.8f} segundos")

def em_segundos(funcao):
    inicio = time.perf_counter()
    funcao()
    fim = time.perf_counter()
    print(f"Tempo: {fim - inicio:.8f} segundos")