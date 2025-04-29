# FORK-CLI

## Setup

**1 - Create python virtual environment**

```bash
python3 -m venv .venv
```

**2 - Activate python virtual environment**

On Windows
```bash
.venv\Scripts\activate
source .venv/bin/activate
```

On Linux
```bash
source .venv/bin/activate
```

**3 - Run Tests**
```
pytest
```

**4 - Run Fork CLI**
```
python3 fork.py
```

## Demanda da Série 3

#### Implemente na linguagem de programação que você pretende usar no curso de Teoria de Grafos as seguintes funções de geração de estrutura de dados para representação de um grafo G=(V,E). Não use bibliotecas de qualquer linguagem na sua implementação, com exceção de funções para visualizar seu grafo.

1. Dado um grafo, gere sua matriz de adjacência;
2. Dado a matriz de adjacência, gere o grafo correspondente;

3. Dado um grafo, gere sua matriz de incidência;
4. Dado uma matriz de incidência, gere o grafo correspondente;

5. Dado um grado, gere sua lista;
6. Dado uma lista, gere o grafo correspondente;

7. Implemente funções que da a descrição de um grafo numa das representações indicadas acima, gere as outras duas representações que vimos em aula.

Para cada um dos subitens acima, descreva como você fez sua implementação.

#### Considerando as estruturas implementadas no exercício anterior, para cada uma das estruturas de dados e grafo correspondente, implemente funções que calcule:

1. O número de vértices de um grafo;
2. O número de arestas de um grafo;
3. Dado um vértice específico, forneça seus vértices adjacentes;
4. Dados dois vértices, retorne se existe uma aresta que os une;
5. Dado um vértice, o seu grau;
6. Dado um grafo, o grau associado a cada vértice;
7. Dado dois vértices específicos, retorne um caminho simples entre eles;
8. Dado um vértice, retorne, se existir, um ciclo no qual ele se situe.
9. Dado um conjunto G’=(V’,E’) e G=(V,E), verificar se G’é subgrafo de G ou vice-versa;

Para cada uma das implementações acima, explique a lógica que você
usou para chegar até as funções.

#### Considere o problema que você escolheu modelar usando uma estrutura de grafo. Use as funções que você desenvolveu na tarefa 2 para achar-lhes as características.

1. Explique como você entra com os conjuntos que compõem a definição deu um grafo;
2. Encontre os vértices de maior e menor grau
3. Considere subconjuntos do seu problema e verifique se eles são subgragos.

#### Considere o grafo que representa todas as rotas de uma companhia aérea sul-americana (Avianca, Azul, Gol, Latam).

1. Use seu pacote predileto para fazer uma representação gráfica de suas rotas.
2. Repita as subtarefas listadas no item 3.
3. Encontre os aeroportos que possuem mais números e menos números de voos.