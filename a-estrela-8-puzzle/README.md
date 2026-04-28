# A* - Jogo dos 8 Números

Trabalho Discente Efetivo 01 da disciplina de **Fundamentos de Inteligência Artificial** da Universidade de Caxias do Sul (UCS).

## Objetivo

Implementar um solucionador automático para o 8-puzzle utilizando o algoritmo de busca **A\*** com duas heurísticas diferentes, comparando seu desempenho.

## Como funciona

O tabuleiro 3x3 possui 8 peças numeradas e um espaço vazio (representado por `0`). O programa encontra a sequência de movimentos para atingir o estado objetivo:

```
1  2  3
4  5  6
7  8  0
```

## Algoritmo

**A\* (A-Estrela):** utiliza a função de custo `f(n) = g(n) + h(n)`, onde:
- `g(n)` — número de movimentos realizados até o estado atual
- `h(n)` — estimativa heurística até o objetivo

### Heurísticas implementadas

- **Manhattan:** soma das distâncias horizontais e verticais de cada peça até sua posição correta
- **Hamming:** conta quantas peças estão fora do lugar

## Como executar

```bash
python Allan_Pedroso_Cunico.py
```

Digite o estado inicial quando solicitado (9 números de 0 a 8 separados por espaço):

```
Estado inicial: 1 2 5 3 4 0 6 7 8
```

## Exemplo de saída

```
--------------------------------------------------
    Heurística Manhattan
--------------------------------------------------
Solução encontrada: Baixo -> Esquerda -> Cima -> ...
Custo da solução: 21
Número de estados visitados: 861
Tempo de execução: 0.0044 segundos
```

## Referência

GARG, Vansh et al. Comparative analysis of AI-based search algorithms in solving 8 puzzle problems. *Bulletin of the National Research Centre*, v. 48, n. 1, p. 1-10, 2024. Disponível em: https://link.springer.com/article/10.1186/s42269-024-01274-3
