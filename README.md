# 📚 Estruturas de Dados

- Site que ajuda a visualizar: https://www.cs.usfca.edu/~galles/visualization/Algorithms.html
- Para ter acesso aos PDFs com explicações: https://shre.ink/SoC1

# 📑 Índice — Estruturas de Dados

- [📚 Introdução](#-introdução)
- [🔹 Vetores](#-vetores)
- [🔹 Vetores Ordenados](#-vetores-ordenados)
- [🔹 Pilhas (LIFO)](#-pilhas-lifo)
- [🔹 Filas (FIFO)](#-filas-fifo)
- [🔹 Fila de Prioridade](#-fila-de-prioridade)
- [🔹 Deque (Double-Ended Queue)](#-deque-double-ended-queue)
- [🔹 Listas Encadeadas](#-listas-encadeadas)

---

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

---

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

---

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

---

## 🔹 Filas
- Uma **fila** é uma estrutura de dados do tipo **FIFO** (*First In, First Out*).  
- Isso significa que **o primeiro elemento que entra é o primeiro a sair**.  

📌 Imagine uma fila de pessoas esperando em um caixa:  
- A primeira pessoa a chegar é a primeira a ser atendida.  
- Novas pessoas entram no final da fila.  

---

### 🔹 Operações Básicas

#### 1. **Enqueue (Inserir)**
- Adiciona um novo elemento **no final da fila**.  
- Exemplo: uma pessoa entra na fila.  

**Complexidade:**  
- O(1) → inserir no final da fila.  

---

#### 2. **Dequeue (Remover)**
- Remove o elemento **do início da fila**.  
- Exemplo: a pessoa da frente é atendida e sai da fila.  

**Complexidade:**  
- O(1) em implementações com ponteiros ou deque.  
- O(n) se usar lista Python padrão e remover o primeiro elemento.  

---

#### 3. **Peek / Front (Consultar o Início)**
- Olhar qual elemento está **no início da fila** sem removê-lo.  

**Complexidade:**  
- O(1) → acesso direto ao primeiro elemento.  

---

#### 4. **isEmpty (Verificar se está vazia)**
- Confere se a fila tem ou não elementos.  

**Complexidade:**  
- O(1)  

---

### 🔹 Exemplo com Pessoas

📌 Situação:  
- Temos uma fila vazia.  
- Vamos adicionar três pessoas: Ana, Bruno e Carla.  

Passo a passo:  
1. `Enqueue(Ana)` → fila = [Ana]  
2. `Enqueue(Bruno)` → fila = [Ana, Bruno]  
3. `Enqueue(Carla)` → fila = [Ana, Bruno, Carla]  
4. `Dequeue()` → remove Ana → fila = [Bruno, Carla]  
5. `Peek()` → início da fila = Bruno  

---

### 🔹 Exemplo: Envio de Pacotes de Dados

- Em redes, pacotes podem ser enviados em **ordem de chegada** usando uma fila.  
- O pacote que chega primeiro será transmitido primeiro.  

📌 Exemplo:  
1. `Enqueue(Pacote A)` → fila = [A]  
2. `Enqueue(Pacote B)` → fila = [A, B]  
3. `Enqueue(Pacote C)` → fila = [A, B, C]  
4. `Dequeue()` → envia A → fila = [B, C]  

---

### 🔹 Exemplo: Impressora

- A impressora processa documentos **na ordem em que chegam** usando uma fila.  

📌 Exemplo:  
1. `Enqueue(Doc1)` → fila = [Doc1]  
2. `Enqueue(Doc2)` → fila = [Doc1, Doc2]  
3. `Enqueue(Doc3)` → fila = [Doc1, Doc2, Doc3]  
4. `Dequeue()` → imprime Doc1 primeiro.  

---

### 🔹 Fila Circular

- Uma **fila circular** é uma variação da fila comum onde o **último elemento se conecta ao primeiro**.  
- Permite **reaproveitar o espaço vazio** deixado por elementos removidos no início, evitando desperdício de memória.  

📌 Vantagens:
- Otimiza o uso do espaço em implementações de tamanho fixo.  
- Evita o deslocamento constante de elementos como em listas lineares.  

#### Exemplo de Fila Circular
1. Inicializamos uma fila circular de tamanho 5: `[_, _, _, _, _]`  
2. `Enqueue(A)` → `[A, _, _, _, _]`  
3. `Enqueue(B)` → `[A, B, _, _, _]`  
4. `Enqueue(C)` → `[A, B, C, _, _]`  
5. `Dequeue()` → remove A → `[_, B, C, _, _]`  
6. `Enqueue(D)` → `[D, B, C, _, _]` (o espaço vazio no início é reutilizado)  

---

### ⚡ Resumo das Operações

| Operação  | Descrição                          | Complexidade |
|-----------|------------------------------------|--------------|
| Enqueue   | Inserir no final da fila           | O(1)         |
| Dequeue   | Remover do início da fila          | O(1)         |
| Peek      | Consultar o elemento do início    | O(1)         |
| isEmpty   | Verificar se a fila está vazia     | O(1)         |
| Fila Circular | Reaproveita espaço e conecta o final ao início | O(1) |

---

### 🔹 Aplicações
- Gerenciamento de **tarefas em sistemas operacionais**  
- Transmissão de **pacotes de rede**  
- Fila de impressão em **impressoras**  
- Processamento de **mensagens em sistemas distribuídos**  
- Estruturas de buffers circulares em **sistemas embarcados*

---

📌 **Resumo intuitivo:**  
A fila é como uma fila de pessoas ou pacotes:  
- O primeiro que entra é o **primeiro a sair** (**FIFO**).  
- Novos elementos entram **no final** da fila. 
- Na **fila circular**, o espaço é reutilizado, tornando a fila mais eficiente.

---

## 🔹 Fila de Prioridade
- Diferente da fila comum (**FIFO**), onde a ordem é a de chegada,  
  na **fila de prioridade** cada elemento tem uma **prioridade associada**.  
- O elemento com **maior prioridade** é atendido primeiro.  
- Se dois elementos têm a mesma prioridade, usa-se a ordem de chegada como critério de desempate.  

📌 Exemplo prático:  
- Em um hospital, pacientes em estado grave são atendidos antes dos demais, mesmo que tenham chegado depois.  

---

### 🔹 Operações Básicas

#### 1. **Inserção (Enqueue com prioridade)**
- Adiciona um novo elemento na fila, levando em conta sua **prioridade**.  
- Pode exigir reorganização da fila (dependendo da implementação).  

**Complexidade:**  
- O(log n) → se usar uma **Heap** (estrutura mais eficiente).  
- O(n) → se percorrer a lista para encontrar a posição correta.  

---

#### 2. **Remoção (Dequeue prioritário)**
- Remove o elemento de **maior prioridade**.  
- Exemplo: em uma emergência, o paciente mais grave é removido da fila para ser atendido.  

**Complexidade:**  
- O(log n) → em implementações com Heap.  
- O(1) → se a fila estiver sempre ordenada (mas a inserção fica mais cara).  

---

#### 3. **Peek (Consultar)**
- Permite visualizar o **elemento de maior prioridade** sem removê-lo.  

**Complexidade:**  
- O(1)  

---

### 🔹 Exemplos Práticos

#### 1. Hospital
- `Enqueue(Paciente Ana, prioridade=2)` → fila = [Ana]  
- `Enqueue(Paciente Bruno, prioridade=5)` → fila = [Bruno, Ana]  
- `Enqueue(Paciente Carla, prioridade=3)` → fila = [Bruno, Carla, Ana]  
- `Dequeue()` → remove Bruno (prioridade mais alta).  

---

#### 2. Impressão com Prioridade
- Documentos importantes podem ter prioridade maior.  
- `Enqueue(Doc1, prioridade=1)`  
- `Enqueue(Doc2, prioridade=10)`  
- `Enqueue(Doc3, prioridade=5)`  
- Ordem de impressão: Doc2 → Doc3 → Doc1.  

---

### 🔹 Fila de Prioridade x Fila Normal

| Tipo                  | Ordem de Atendimento          |
|------------------------|-------------------------------|
| Fila Normal (FIFO)    | Ordem de chegada              |
| Fila de Prioridade    | Ordem de maior prioridade     |

---

### 🔹 Estruturas de Implementação
- **Lista Ordenada:** simples, mas inserção é O(n).  
- **Heap Binária (Min-Heap ou Max-Heap):** eficiente, com inserção e remoção em O(log n).  
- **Fila com múltiplas filas internas:** cada fila representa uma prioridade diferente.  

---

### ⚡ Resumo das Operações

| Operação   | Descrição                                | Complexidade |
|------------|------------------------------------------|--------------|
| Enqueue    | Inserir elemento com prioridade          | O(log n) ou O(n) |
| Dequeue    | Remover elemento de maior prioridade     | O(log n) |
| Peek       | Consultar o elemento de maior prioridade | O(1) |
| isEmpty    | Verificar se a fila está vazia           | O(1) |

---

### 🔹 Aplicações
- **Sistemas Operacionais** → escalonamento de processos (processos críticos rodam antes).  
- **Redes de Computadores** → pacotes urgentes transmitidos primeiro.  
- **Simulações** → eventos com prioridade maior são processados antes.  
- **Atendimento em Hospitais ou Call Centers** → casos urgentes são tratados antes.  
- **Algoritmos de Grafos** → Dijkstra e A* usam filas de prioridade para explorar vértices com menor custo primeiro.  

---

📌 **Resumo intuitivo:**  
A **fila de prioridade** funciona como um hospital ou sistema de emergência:  
- Nem sempre o primeiro a chegar é o primeiro a sair.  
- O **mais urgente (maior prioridade)** é atendido primeiro.  

---

## 🔹 Deque
- Um **Deque** (*Double-Ended Queue*) é uma estrutura de dados que permite **inserir e remover elementos tanto no início quanto no final**.  
- Ele é considerado uma **junção de Fila (FIFO)** e **Pilha (LIFO)**:
  - Como **fila** → elementos entram no final e saem no início.  
  - Como **pilha** → elementos entram e saem no mesmo lado (topo).  

📌 Em resumo, o Deque é **mais flexível** que Pilha e Fila, pois combina as operações de ambas.

---

### 🔹 Implementações de um Deque
Um Deque pode ser implementado de diferentes formas:

1. **Estático**  
   - Utiliza um **vetor de tamanho fixo**.  
   - Necessita controle manual dos índices de início e fim.  
   - Pode sofrer desperdício de espaço se não for circular.  

2. **Circular**  
   - O final do vetor está conectado ao início.  
   - Permite **reaproveitar espaços** liberados quando elementos são removidos.  
   - Muito eficiente em termos de **uso de memória**.  

---

### 🔹 Operações e Complexidade

| Operação              | Descrição                                 | Complexidade |
|------------------------|-------------------------------------------|--------------|
| `append(valor)`        | Inserir elemento no **final**             | O(1) |
| `appendleft(valor)`    | Inserir elemento no **início**            | O(1) |
| `pop()`                | Remover elemento do **final**             | O(1) |
| `popleft()`            | Remover elemento do **início**            | O(1) |
| `peek()`               | Consultar o último elemento               | O(1) |
| `peekleft()`           | Consultar o primeiro elemento             | O(1) |
| `isEmpty()`            | Verificar se está vazio                   | O(1) |

---

### ⚡ Comparação: Pilha, Fila e Deque

| Estrutura | Inserção       | Remoção       | Restrição            |
|-----------|----------------|---------------|----------------------|
| **Fila**  | Final          | Início        | FIFO                 |
| **Pilha** | Topo           | Topo          | LIFO                 |
| **Deque** | Início e Final | Início e Final| Combina FIFO e LIFO  |

---

### 🔹 Aplicações do Deque
- Filas de prioridade  
- Agendamento de tarefas em multiprocessadores  
- Algoritmo de **agendamento de trabalho furtivo (work-stealing)**  
  - Usado na biblioteca **Threading Building Blocks (TBB)** da **Intel** para programação paralela  
- Buffers circulares (ex: streaming de áudio/vídeo)  
- Algoritmos de **sliding window** (ex: máximo/mínimo em janelas móveis)  

---

### 📌 Resumo intuitivo
- O **Deque** é como uma fila que pode ser usada **dos dois lados**.  
- Ele pode ser implementado de forma **estática** (vetor fixo) ou **circular** (aproveitamento máximo do espaço).  
- Combina o melhor de **pilhas** e **filas** numa única estrutura, com operações rápidas (**O(1)**).

---

## 🔹 Listas Encadeadas

### 1. **Pesquisa Linear**
- Para encontrar um elemento, percorremos a lista do início até achar o valor ou chegar ao final.  
- **Complexidade:** O(n), pois no pior caso precisamos percorrer todos os elementos.  

---

### 2. **Inserção no Início**
- Criamos um novo nó.  
- O ponteiro do novo nó aponta para o antigo primeiro nó.  
- O início da lista passa a ser o novo nó.  
- **Complexidade:** O(1), pois não depende do tamanho da lista.  

---

### 3. **Remoção no Início**
- Guardamos a referência do primeiro nó.  
- Fazemos o início da lista apontar para o segundo nó.  
- Liberamos o antigo nó.  
- **Complexidade:** O(1), pois só alteramos ponteiros.  

---

### 4. **Exclusão em uma Posição Específica**
- Percorremos a lista até o nó anterior à posição desejada.  
- Ajustamos o ponteiro dele para "pular" o nó a ser removido.  
- **Complexidade:** O(n), pois precisamos percorrer até a posição desejada.  

---

### 5. **Mostrar a Lista**
- Percorremos do início até o final imprimindo os valores.  
- **Complexidade:** O(n), pois percorremos todos os elementos.  

---

### ⚡ Complexidade das Operações

| Operação             | Complexidade |
|-----------------------|--------------|
| Inserção no início    | O(1)         |
| Remoção no início     | O(1)         |
| Exclusão na posição   | O(n)         |
| Pesquisa (linear)     | O(n)         |
| Mostrar lista         | O(n)         |

---

### 🔹 Aplicações
- Estruturas dinâmicas em linguagens de programação  
- Implementação de **pilhas** e **filas**  
- Gerenciamento de **memória dinâmica**  
- Algoritmos que precisam de inserções e remoções frequentes no meio da lista  

---

### 📌 Resumo intuitivo
A lista encadeada é como uma corrente de elos:  
- Cada elo aponta para o próximo.  
- Para acessar o 5º elo, você precisa passar pelo 1º, 2º, 3º e 4º.  
- Inserir ou remover no início é rápido, mas localizar elementos exige percorrer.  

---

## 🔹 Listas Encadeadas com Extremidades Duplas

Uma **lista encadeada com extremidades duplas** mantém ponteiros tanto para o **primeiro nó** (*head*) quanto para o **último nó** (*tail*).  
Isso facilita algumas operações, como inserir no final, sem precisar percorrer toda a lista.

---

### 1. **Inserção no Início**
- Criamos um novo nó.  
- O ponteiro do novo nó aponta para o antigo primeiro nó.  
- O início da lista passa a ser o novo nó.  
- Se a lista estava vazia, o final também passa a apontar para esse nó.  
- **Complexidade:** O(1), não depende do tamanho da lista.  

---

### 2. **Inserção no Final**
- Criamos um novo nó.  
- O ponteiro do último nó (tail) passa a apontar para o novo nó.  
- Atualizamos o ponteiro de **final** para o novo nó.  
- Se a lista estava vazia, o início também aponta para ele.  
- **Complexidade:** O(1), pois acessamos o final diretamente.  

---

### 3. **Remoção no Início**
- Guardamos a referência do primeiro nó.  
- O início da lista passa a apontar para o próximo nó.  
- Se a lista ficar vazia, o final também é atualizado para `null`.  
- Liberamos o antigo nó.  
- **Complexidade:** O(1), só ajustamos ponteiros.  

---

### 4. **Por que não é possível remover no Final?**
- Apesar de termos um ponteiro para o **último nó** (*tail*), não temos acesso direto ao **nó anterior**.  
- Em uma lista **simplesmente encadeada**, cada nó só conhece o **próximo**, nunca o anterior.  
- Para excluir o último nó, seria necessário percorrer a lista inteira até encontrar o penúltimo nó.  
- Assim, a operação teria **complexidade O(n)**.  

👉 Por isso, em listas **simples** com extremidades duplas, **não é eficiente remover no final**.  
Se quisermos remoção eficiente no final, precisamos usar uma **lista duplamente encadeada**, onde cada nó conhece tanto o **próximo** quanto o **anterior**.  

---

### 5. **Mostrar a Lista**
- Percorremos do início até o fim imprimindo os valores.  
- **Complexidade:** O(n), pois percorremos todos os elementos.  

---

### ⚡ Complexidade das Operações

| Operação             | Complexidade |
|-----------------------|--------------|
| Inserção no início    | O(1)         |
| Inserção no final     | O(1)         |
| Remoção no início     | O(1)         |
| Mostrar lista         | O(n)         |

---

### 🔹 Aplicações
- Estruturas de **filas** (inserção no final, remoção no início).  
- Gerenciamento de **buffers de dados**.  
- Estruturas dinâmicas que exigem acesso rápido ao início e ao final.  

---

### 📌 Resumo intuitivo
A lista encadeada com extremidades duplas é como uma **fila de pessoas**:  
- Você pode adicionar alguém no **início** ou no **final** rapidamente.  
- Para ver todos, é preciso percorrer da primeira até a última pessoa.  

---

## 🔹 Listas Duplamente Encadeadas

Uma **lista duplamente encadeada** é uma variação da lista encadeada em que cada nó possui **dois ponteiros**:  
- Um que aponta para o **próximo** nó.  
- Outro que aponta para o **anterior**.  

Além disso, a lista mantém referências para o **primeiro** (*head*) e para o **último** (*tail*) nó.  
Isso permite inserir e remover elementos tanto no início quanto no final de forma eficiente.

---

### 1. **Inserção no Início**
- Criamos um novo nó.  
- O novo nó aponta para o antigo primeiro nó.  
- O ponteiro `anterior` do antigo primeiro nó passa a apontar para o novo.  
- Atualizamos o ponteiro de início para o novo nó.  
- Se a lista estava vazia, o final também passa a ser o novo nó.  
- **Complexidade:** O(1).  

---

### 2. **Inserção no Final**
- Criamos um novo nó.  
- O novo nó aponta para `None` como próximo.  
- O `anterior` do novo nó aponta para o antigo último nó.  
- O `próximo` do último nó passa a apontar para o novo nó.  
- Atualizamos o ponteiro de final para o novo nó.  
- Se a lista estava vazia, o início também passa a ser o novo nó.  
- **Complexidade:** O(1).  

---

### 3. **Remoção no Início**
- Guardamos a referência do primeiro nó.  
- O início passa a apontar para o segundo nó.  
- O ponteiro `anterior` do novo primeiro nó é atualizado para `None`.  
- Se a lista ficar vazia, o final também é atualizado para `None`.  
- **Complexidade:** O(1).  

---

### 4. **Remoção no Final**
- Guardamos a referência do último nó.  
- O final passa a ser o nó anterior.  
- O `próximo` do novo último nó é atualizado para `None`.  
- Se a lista ficar vazia, o início também é atualizado para `None`.  
- **Complexidade:** O(1).  

---

### 5. **Remoção em uma Posição Específica**
- Percorremos a lista até chegar ao nó da posição desejada.  
- Ajustamos os ponteiros:
  - O `próximo` do nó anterior passa a apontar para o nó seguinte.  
  - O `anterior` do nó seguinte passa a apontar para o nó anterior.  
- Se for o primeiro nó, usamos a lógica de **remoção no início**.  
- Se for o último nó, usamos a lógica de **remoção no final**.  
- **Complexidade:** O(n), pois pode ser necessário percorrer a lista até a posição desejada.  

---

### 6. **Mostrar a Lista**
- Percorremos do início até o final imprimindo os valores.  
- **Complexidade:** O(n), pois percorremos todos os elementos.  

---

### ⚡ Complexidade das Operações

| Operação                   | Complexidade |
|-----------------------------|--------------|
| Inserção no início          | O(1)         |
| Inserção no final           | O(1)         |
| Remoção no início           | O(1)         |
| Remoção no final            | O(1)         |
| Remoção em posição específica | O(n)       |
| Mostrar lista               | O(n)         |

---

### 🔹 Diferença para Lista Simplesmente Encadeada
- **Lista Simplesmente Encadeada**: cada nó só conhece o **próximo**.  
  - Inserir no final é rápido (O(1)), mas remover no final é **lento (O(n))**, pois precisamos percorrer até o penúltimo nó.  
  - Remover em uma posição específica também exige percorrer até chegar nela.  

- **Lista Duplamente Encadeada**: cada nó conhece tanto o **próximo** quanto o **anterior**.  
  - Isso permite **remoção eficiente no final (O(1))**, além de facilitar percorrer a lista nos dois sentidos.  
  - Mesmo assim, para remover em uma posição arbitrária ainda precisamos percorrer até ela (O(n)).  

---

### 🔹 Aplicações
- Estruturas de **deque** (fila dupla, com inserção e remoção em ambas as extremidades).  
- Navegação em **listas de histórico** (avançar e voltar).  
- Estruturas que exigem inserções e remoções frequentes em ambas as pontas.  

---

### 📌 Resumo intuitivo
A lista duplamente encadeada é como uma **linha de pessoas de mãos dadas**:  
- Cada pessoa segura a mão da próxima **e** da anterior.  
- Assim, é fácil remover alguém tanto do **início** quanto do **final**, sem precisar andar pela fila inteira.  
- Mas, para remover alguém do **meio da fila**, ainda precisamos andar até ela.  

---

## 🔹 Pilhas e Filas com Listas Simplesmente Encadeadas

Uma **lista simplesmente encadeada** é composta por nós que armazenam:  
- Um **valor**.  
- Um ponteiro para o **próximo nó**.  

Diferente de um **array/vetor**, a lista encadeada não precisa de espaço contíguo na memória.  
Isso traz vantagens na implementação de **pilhas (LIFO)** e **filas (FIFO)**.  

---

### 1. **Pilha com Lista Encadeada**
A pilha segue o princípio **LIFO (Last In, First Out)**: o último a entrar é o primeiro a sair.  

- **Inserção (push)**:  
  - O novo nó é adicionado sempre no **início** da lista.  
  - O ponteiro `próximo` do novo nó aponta para o antigo topo.  
  - Atualizamos o **topo** para esse novo nó.  
  - **Complexidade:** O(1).  

- **Remoção (pop)**:  
  - Removemos sempre o **início** da lista.  
  - Atualizamos o ponteiro `topo` para o próximo nó.  
  - **Complexidade:** O(1).  

✅ **Vantagem sobre arrays**: não há necessidade de realocar memória ou lidar com limite fixo de tamanho.  

---

### 2. **Fila com Lista Encadeada**
A fila segue o princípio **FIFO (First In, First Out)**: o primeiro a entrar é o primeiro a sair.  

- **Inserção (enqueue)**:  
  - O novo nó é adicionado sempre no **final** da lista.  
  - O ponteiro `próximo` do antigo último nó passa a apontar para o novo nó.  
  - Atualizamos a referência de **último** para o novo nó.  
  - **Complexidade:** O(1).  

- **Remoção (dequeue)**:  
  - Removemos sempre o **início** da lista.  
  - Atualizamos o ponteiro `primeiro` para o próximo nó.  
  - **Complexidade:** O(1).  

✅ **Vantagem sobre arrays**: em arrays, a remoção no início custa **O(n)** (pois todos os elementos precisam ser deslocados).  
Na lista encadeada, basta ajustar o ponteiro.  

---

### ⚡ Complexidade das Operações

| Estrutura | Operação          | Complexidade |
|-----------|-------------------|--------------|
| **Pilha** | Push (inserir)    | O(1)         |
|           | Pop (remover)     | O(1)         |
| **Fila**  | Enqueue (inserir) | O(1)         |
|           | Dequeue (remover) | O(1)         |

---

### 🔹 Vantagens da Lista Encadeada
- **Memória dinâmica**: cresce e diminui conforme a necessidade, sem limite fixo.  
- **Eficiência nas operações**: inserções e remoções no início ou no fim custam **O(1)**.  
- **Sem deslocamentos**: diferente dos arrays, não é preciso mover elementos.  

---

### 📌 Resumo intuitivo
- **Pilha com lista encadeada** → pense em uma **pilha de pratos**, onde você sempre coloca e tira do **topo**.  
- **Fila com lista encadeada** → pense em uma **fila de pessoas**, onde entra gente no **fim** e sai gente pelo **início**.  

👉 A lista encadeada é como se cada prato ou pessoa tivesse um "cartão" dizendo quem vem depois.  
Isso evita o trabalho de reorganizar todo o conjunto sempre que alguém entra ou sai.  

---

## 🔹 Recursão

A **recursão** é uma técnica em que uma função **chama a si mesma** para resolver um problema. Ela divide o problema em **subproblemas menores**, até chegar a um **caso base**, que interrompe a recursão.

---

### 1. **Exemplo: Fatorial**

```python
def fatorial(n):
    if n == 0:  # Caso base
        return 1
    return n * fatorial(n - 1)  # Chamada recursiva
```
   
- fatorial(5) chama fatorial(4) → chama fatorial(3) → até chegar em fatorial(0).

### 2. **Árvore de Execução**

Cada chamada recursiva cria uma camada de execução (stack frame) na memória. 
Quando o caso base é atingido, a pilha começa a ser desempilhada, retornando os valores.

- fatorial(3) → 3 * fatorial(2) → 3 * (2 * fatorial(1)) → 3 * (2 * (1 * fatorial(0))) → 3 * 2 * 1 * 1 = 6

### 3. **Complexidade Big-O da Recursão**

A análise de complexidade depende de quantas vezes a função é chamada e o custo de cada chamada.

🔹 Exemplo 1: Fatorial

```python
def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n - 1)
```
- Cada chamada reduz n em 1. Temos n chamadas até chegar no caso base.
- Complexidade: O(n)

🔹 Exemplo 2: Fibonacci (recursivo simples)

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```
- Cada chamada gera duas novas chamadas. O número de chamadas cresce exponencialmente.
- Complexidade: O(2^n) (muito ineficiente).

🔹 Exemplo 3: Busca Binária (recursiva)

```python
def busca_binaria(arr, inicio, fim, x):
    if inicio > fim:
        return -1
    meio = (inicio + fim) // 2
    if arr[meio] == x:
        return meio
    elif arr[meio] > x:
        return busca_binaria(arr, inicio, meio - 1, x)
    else:
        return busca_binaria(arr, meio + 1, fim, x)
```
- A cada chamada, o problema é dividido pela metade.
- Complexidade: O(log n)

### ⚡ Tabela de Complexidade da Recursão

| Algoritmo          | Complexidade |
|--------------------|--------------|
| Fatorial           | O(n)         |
| Fibonacci simples  | O(2^n)       |
| Busca Binária      | O(log n)     |
| Quicksort (média)  | O(n log n)   |
| Quicksort (pior)   | O(n²)        |

---

### 🔹 Vantagens da Recursão
- Código mais elegante e legível para problemas que se dividem naturalmente (ex: árvores, divisão e conquista).  
- Evita laços complexos em problemas de múltiplos níveis.  

---

### 🔹 Desvantagens
- Pode ser menos eficiente que a versão iterativa (uso extra de memória na pilha de chamadas).  
- Risco de **estouro de pilha (stack overflow)** se o caso base não for bem definido.  

---

### 📌 Resumo Intuitivo
A recursão é como **espelhos frente a frente**:  

Cada espelho reflete o próximo até que a imagem fique tão pequena que desaparece (**caso base**).  

O custo depende de quantas vezes você reflete e o que faz em cada reflexão.  

---

# 🧩 Ordenação de Vetores (Sorting)

A **ordenação de vetores** é uma das operações mais importantes em ciência da computação.  
Ela organiza os elementos de um conjunto (como números, nomes ou objetos) em uma sequência lógica — normalmente **crescente ou decrescente**.

---

## 🎯 Por que precisamos ordenar?

A ordenação é essencial porque:

- 🔍 **Facilita a busca** — algoritmos de busca binária, por exemplo, só funcionam em listas ordenadas.  
- 📊 **Melhora a análise de dados** — dados organizados são mais fáceis de interpretar e visualizar.  
- ⚙️ **Aumenta a eficiência de outros algoritmos** — muitas estruturas de dados e operações (como junções em bancos de dados) se beneficiam de listas ordenadas.  
- 📦 **Otimiza tarefas práticas** — como exibir rankings, listas de preços, resultados de pesquisas, ou organizar arquivos por data/nome.  

---

## 🌍 Onde é útil?

- Sistemas de recomendação (ordenar produtos ou filmes por relevância)  
- Processamento de grandes volumes de dados  
- Aplicações financeiras (ordenar transações, preços, históricos)  
- Jogos (ordenar pontuações, ranking de jogadores)  

---

## 🔗 Visualização on-line

Você pode ver como os algoritmos de ordenação funcionam de forma interativa neste site:

👉 [**Visualização on-line de Ordenações – Visualgo**](https://visualgo.net/en/sorting)

---

## 🫧 Ordenação Bubble Sort (Método da Bolha)

O **Bubble Sort**, também chamado de **método da bolha**, é um dos algoritmos de ordenação mais simples de entender.

---

### ⚙️ Como funciona

1. O algoritmo percorre o vetor várias vezes.  
2. Em cada passagem, ele compara **pares de elementos adjacentes**.  
3. Se o elemento da esquerda for **maior que o da direita**, eles são trocados.  
4. A cada passagem, o **maior elemento “sobe”** para o final do vetor, como uma bolha subindo na água.  
5. O processo se repete até que não haja mais trocas — o vetor está ordenado.

---

### 📈 Análise de desempenho

Para um vetor com **10 elementos**, ele faz:

````yaml
9 comparações na 1ª passagem
8 na 2ª
7 na 3ª
… até 1 comparação na última
````

**Total de comparações:**
9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 = 45

---

### 💡 Big-O (Complexidade)

- **O(n²)** — cresce quadraticamente com o tamanho do vetor.  
- Faz cerca de **N² / 2 comparações**.  
- Há menos trocas que comparações, pois só há troca quando dois elementos estão fora de ordem.  
- Se os dados estiverem aleatórios, o número médio de trocas será aproximadamente **N² / 4**.  
- No pior caso (vetor em ordem inversa), quase toda comparação resulta em troca.

---

### 🧠 Onde é aplicável

Apesar de ineficiente para grandes volumes de dados, o **Bubble Sort** é útil para:

- 🧩 Ensinar conceitos básicos de ordenação e comparação.  
- 📋 Pequenas listas (onde a simplicidade importa mais que o desempenho).  
- ⚡ Situações em que é importante detectar rapidamente se o vetor já está ordenado (o algoritmo pode parar mais cedo).  

---

## 🔍 Ordenação Selection Sort (Método da Seleção)

O **Selection Sort**, também conhecido como **método da seleção**, é um algoritmo de ordenação simples que **seleciona o menor elemento** de uma lista e o coloca na **posição correta**, repetindo esse processo até que todos os elementos estejam ordenados.

---

### ⚙️ Como funciona

1. O algoritmo percorre o vetor procurando o **menor elemento**.  
2. Ao encontrá-lo, **troca-o** com o elemento da posição inicial.  
3. Em seguida, ignora a primeira posição (já ordenada) e **repete o processo** com o restante do vetor.  
4. O processo se repete até o último elemento — que automaticamente estará no lugar correto.

---

### 📊 Exemplo de comportamento

Para um vetor com **10 elementos**, o Selection Sort faz:

````yaml
9 comparações na 1ª passagem  
8 comparações na 2ª  
7 na 3ª  
… até 1 na última
````

### 📊 Total de comparações
9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 = 45

### 🧮 Complexidade Big-O
- **Tempo:** `O(n²)`  
- **Comparações:** cerca de `N² / 2`, exatamente como o **Bubble Sort**  
- **Trocas:** muito menores — geralmente **uma por passagem**

#### 📈 Exemplos práticos:
- Com **10 elementos** → menos de **10 trocas**  
- Com **100 elementos** → cerca de **4.950 comparações**, mas menos de **100 trocas**

---

## ⚡ Diferença entre Selection Sort e Bubble Sort

| Aspecto | 🫧 **Bubble Sort** | 🔍 **Selection Sort** |
|----------|--------------------|----------------------|
| **Comparações** | Muitas (`N² / 2`) | Muitas (`N² / 2`) |
| **Trocas** | Muitas (até `N² / 4`) | Poucas (≈ `N`) |
| **Eficiência** | Mais lento em listas grandes | Um pouco mais eficiente |
| **Estratégia** | Compara pares adjacentes e troca várias vezes | Seleciona o menor e faz uma única troca por passagem |
| **Detecta vetor ordenado** | ✅ Sim (pode parar antes) | ❌ Não (percorre até o final sempre) |
| **Didática** | Excelente para aprender **trocas e comparações** | Boa para entender **seleção e posição fixa** |

---

## 💡 Quando usar

O **Selection Sort** é mais indicado quando:

- 🧠 O foco é **entendimento de algoritmos**, não desempenho.  
- 🧩 As listas são **pequenas**, e a simplicidade é mais importante que a velocidade.  
- 📉 Há necessidade de **minimizar trocas**, por exemplo, quando mover elementos é custoso.

---

## 🔗 Visualização online

Você pode visualizar o funcionamento do **Selection Sort** (e comparar com o Bubble Sort) neste link interativo:

👉 [Visualização de algoritmos de ordenação (Visualgo)](https://visualgo.net/en/sorting)

---