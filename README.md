# 📚 Estruturas de Dados

- Site que ajuda a visualizar: https://www.cs.usfca.edu/~galles/visualization/Algorithms.html


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
