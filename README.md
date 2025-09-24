# 📚 Estruturas de Dados

- Site que ajuda a visualizar: https://www.cs.usfca.edu/~galles/visualization/Algorithms.html
- Para ter acesso aos PDFs com explicações: https://shre.ink/SoC1


## 🔹 Vetores
- Um **vetor** (ou *array*) é uma estrutura de dados **estática** que armazena elementos do mesmo tipo em posições contíguas da memória.  
- Cada elemento pode ser acessado por um **índice** (geralmente começando em `0`).  

✅ **Vantagens**: acesso direto a qualquer posição em tempo constante → **O(1)**.  
⚠️ **Desvantagens**: tamanho fixo e custo elevado em inserções/remoções fora do final.  

---

### 🔹 Pesquisa Linear
- Também chamada de **busca sequencial**.  
- Percorre o vetor elemento por elemento até encontrar o valor desejado ou chegar ao final.  

**Complexidade:**
- Melhor caso: **O(1)** → elemento encontrado logo no início.  
- Pior caso: **O(n)** → elemento está no final ou não existe.  

---

### 🔹 Inserção
- Inserir no **final do vetor**: **O(1)** (não há deslocamento).  
- Inserir no **início ou meio**: **O(n)** (necessário deslocar os elementos à direita).  

---

### 🔹 Remoção
- Remover no **final do vetor**: **O(1)** (basta descartar o último elemento).  
- Remover no **início ou meio**: **O(n)** (necessário deslocar os elementos à esquerda).  

---

### ⚡ Resumo das Operações

| Operação         | Melhor Caso | Pior Caso |
|------------------|-------------|-----------|
| Acesso (índice)  | O(1)        | O(1)      |
| Pesquisa Linear  | O(1)        | O(n)      |
| Inserção         | O(1)        | O(n)      |
| Remoção          | O(1)        | O(n)      |

## 🔹 Vetores Ordenados
- Um **vetor ordenado** é semelhante a um vetor comum, mas seus elementos são mantidos em **ordem crescente ou decrescente**.  
- Essa ordenação permite o uso de algoritmos de busca mais eficientes, como a **pesquisa binária**.  

✅ **Vantagens**: possibilita busca mais rápida com **O(log n)** usando pesquisa binária.  
⚠️ **Desvantagens**: inserções e remoções continuam custosas, pois precisam manter a ordem → **O(n)**.  

---

### 🔹 Pesquisa Linear
- Mesmo em vetores ordenados, ainda é possível realizar a **busca sequencial**.  
- Percorre o vetor elemento por elemento até encontrar o valor ou chegar ao final.  

**Complexidade:**
- Melhor caso: **O(1)** → elemento encontrado logo no início.  
- Pior caso: **O(n)** → elemento está no final ou não existe.  

---

### 🔹 Pesquisa Binária
- Mais eficiente que a pesquisa linear em vetores ordenados.  
- Divide o vetor repetidamente pela metade, descartando a metade que não contém o elemento procurado.  
- Exige que o vetor esteja **previamente ordenado**.  

**Complexidade:**
- Melhor caso: **O(1)** → elemento encontrado logo na primeira comparação.  
- Pior caso: **O(log n)** → espaço de busca é reduzido pela metade a cada passo. 

#### 🔍 (Exemplo Simplificado)

• Números de 1 até 100  
• Pesquisar o número **47**  

• 1 até 100 / 2 = 50  
• 50 é o número pesquisado? **Não**  
• 47 é menor ou maior do que 50? **Menor**  

• 1 até 49 / 2 = 25  
• 25 é o número pesquisado? **Não**  
• 47 é menor ou maior do que 25? **Maior**  

• 26 até 49 / 2 = 38  
• 38 é o número pesquisado? **Não**  
• 47 é menor ou maior do que 38? **Maior**  

• 39 até 49 / 2 = 44  
• 44 é o número pesquisado? **Não**  
• 47 é menor ou maior do que 44? **Maior**  

• 45 até 49 / 2 = 47  
• 47 é o número pesquisado? **Sim ✅**  

* Total de 9 passos, com a pesquisa linear seriam 47 passos.

#### 🔍 Pesquisa Binária x Pesquisa Linear

| Faixa            | Comparações Binária | Comparações Linear (N/2) |
|------------------|----------------------|---------------------------|
| 10               | 4                    | 5                         |
| 100              | 7                    | 50                        |
| 1.000            | 10                   | 500                       |
| 10.000           | 14                   | 5.000                     |
| 100.000          | 17                   | 50.000                    |
| 1.000.000        | 20                   | 500.000                   |
| 10.000.000       | 24                   | 5.000.000                 |
| 100.000.000      | 27                   | 50.000.000                |
| 1.000.000.000    | 30                   | 500.000.000               |

---

### 🔹 Inserção
- Para manter a ordenação, é necessário encontrar a posição correta do novo elemento.  
- Após encontrar a posição, todos os elementos à direita precisam ser **deslocados**.  

**Complexidade:**
- Inserção: **O(n)** (devido ao deslocamento, mesmo que a busca da posição seja feita em O(log n)).  

---

### 🔹 Remoção
- Para remover, primeiro é necessário localizar o elemento (pode ser feito em **O(log n)** com pesquisa binária).  
- Em seguida, todos os elementos à direita precisam ser **deslocados** para preencher o espaço.  

**Complexidade:**
- Remoção: **O(n)** (pelo deslocamento, mesmo que a busca seja rápida).  

---

### ⚡ Resumo das Operações

| Operação          | Melhor Caso | Pior Caso |
|-------------------|-------------|-----------|
| Acesso (índice)   | O(1)        | O(1)      |
| Pesquisa Linear   | O(1)        | O(n)      |
| Pesquisa Binária  | O(1)        | O(log n)  |
| Inserção          | O(n)        | O(n)      |
| Remoção           | O(n)        | O(n)      |

## 🔹 Pilhas
- Uma **pilha** é uma estrutura de dados do tipo **LIFO** (*Last In, First Out*).  
- Isso significa que **o último elemento que entra é o primeiro a sair**.  

📌 Imagine uma pilha de **moedas**:  
- Você só consegue **colocar** uma moeda no topo.  
- E só consegue **retirar** a moeda que está no topo.  

---

### 🔹 Operações Básicas

#### 1. **Push (Empilhar)**
- Adiciona um novo elemento no **topo** da pilha.  
- Exemplo: colocar uma nova moeda no topo da pilha.  

**Complexidade:**  
- Sempre **O(1)** → basta inserir no topo.  

---

#### 2. **Pop (Desempilhar)**
- Remove o elemento do **topo** da pilha.  
- Exemplo: retirar a moeda que está no topo da pilha.  

**Complexidade:**  
- Sempre **O(1)** → basta remover o último inserido.  

---

#### 3. **Peek / Top (Consultar o Topo)**
- Olhar qual elemento está no topo sem removê-lo.  
- Exemplo: ver qual moeda está por cima da pilha.  

**Complexidade:**  
- Sempre **O(1)**.  

---

#### 4. **isEmpty (Verificar se está vazia)**
- Confere se a pilha tem ou não elementos.  

**Complexidade:**  
- Sempre **O(1)**.  

---

### 🔹 Exemplo com Moedas

📌 Situação:  
- Temos uma pilha vazia.  
- Vamos empilhar as moedas de **1 real**, **50 centavos** e **25 centavos**.  

Passo a passo:  
1. `Push(1 real)` → pilha = [1]  
2. `Push(0,50)` → pilha = [1, 0,50]  
3. `Push(0,25)` → pilha = [1, 0,50, 0,25]  
4. `Pop()` → remove 0,25 → pilha = [1, 0,50]  
5. `Peek()` → topo = 0,50  

---

### ⚡ Resumo das Operações

| Operação  | Descrição                        | Complexidade |
|-----------|----------------------------------|--------------|
| Push      | Inserir no topo da pilha         | O(1)         |
| Pop       | Remover do topo da pilha         | O(1)         |
| Peek      | Consultar o elemento do topo     | O(1)         |
| isEmpty   | Verificar se a pilha está vazia  | O(1)         |

---

### 🔹 Aplicações
- Correção de expressões aritméticas, tais como `3 * (4 + 5)`  
- Percorrimento de uma **árvore binária**  
- Pesquisa do vértice de um **grafo**  
- **Microprocessadores** com arquitetura baseada em pilhas:  
  - Quando um método é chamado, seu endereço de retorno e seus parâmetros são empilhados em uma pilha.  
  - Quando ele retorna, esses valores são desempilhados. 

---

📌 **Resumo intuitivo:**  
A pilha é como uma pilha de moedas ou pratos:  
- Só dá para mexer no **topo**.  
- O que entrou por último, sai primeiro (**LIFO**).  

