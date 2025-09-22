import numpy as np
import  matplotlib.pyplot as plt

n = np.linspace(1, 10, 100) # gerar números espaçados

len(n) # tamanho da lista

labels = ['Constant', 'Logarithmic', 'Linear', 'Log Linear', 'Quadratic', 'Cubic', 'Exponential']

big_o = [
    np.ones(n.shape),   # constante
    np.log(n),          # logarítmica
    n,                  # linear
    n * np.log(n),      # log linear
    n**2,               # quadrática
    n**3,               # cúbica
    2**n                # exponencial
]

plt.figure(figsize=(10, 8))  # tamanho do gráfico
plt.ylim(0, 100)  # limite do eixo y


for indice in range(len(big_o)):
    funcao = big_o[indice]
    plt.plot(n, funcao, label=labels[indice])  # plota cada curva com legenda

plt.legend()
plt.xlabel("n")
plt.ylabel("Complexidade")
plt.title("Notação Big-O")
plt.grid(True)

plt.show()  # para exibir o gráfico