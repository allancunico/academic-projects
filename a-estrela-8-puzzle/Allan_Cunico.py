#--------------------------------------------------------------------------------------------------------
# Allan Pedroso Cunico
# TDE 1 - Resolvendo o Jogo dos 8 Números
#--------------------------------------------------------------------------------------------------------

import heapq  # Fila de prioridade (min-heap)
import time   # Para medir o tempo de execução

OBJETIVO = (1, 2, 3, 4, 5, 6, 7, 8, 0)

#--------------------------------------------------------------------------------------------------------
# VERIFICA POSSIBILIDADE DE RESOLVER O JOGO
#--------------------------------------------------------------------------------------------------------

def contar_inversoes(tabuleiro):
    """Conta o número de inversões no estado atual do tabuleiro."""
    
    inversoes = 0
    for i in range(len(tabuleiro)):
        for j in range(i + 1, len(tabuleiro)):
            if tabuleiro[i] != 0 and tabuleiro[j] != 0 and tabuleiro[i] > tabuleiro[j]:
                inversoes += 1
    
    return inversoes

def eh_resolvivel(tabuleiro):
    """Verifica se o estado atual do tabuleiro é resolvível.
    Um estado é resolvível se o número de inversões for par.
    """
    return contar_inversoes(tabuleiro) % 2 == 0

#--------------------------------------------------------------------------------------------------------
# FUNCOES HEURÍSTICAS
#--------------------------------------------------------------------------------------------------------

def heuristica_manhattan(tabuleiro):
    """Heurística de Manhattan: Soma das distâncias de cada peça até sua posição correta."""
    
    distancia = 0
    
    for i in range(9):
        if tabuleiro[i] != 0:
            valor = tabuleiro[i]
            pos_objetivo = valor - 1
            distancia += abs(i // 3 - pos_objetivo // 3) + abs(i % 3 - pos_objetivo % 3)
    
    return distancia

def heuristica_hamming(tabuleiro):
    """Heurística de Hamming: Conta o número de peças que não estão na posição correta."""
    
    erradas = 0
    
    for i in range(9):
        if tabuleiro[i] != 0 and tabuleiro[i] != OBJETIVO[i]:
            erradas += 1
    
    return erradas

#--------------------------------------------------------------------------------------------------------
# MOVIMENTOS E RESTRIÇÕES
#--------------------------------------------------------------------------------------------------------

MOVES = {
    "Cima": -3,
    "Baixo": 3,
    "Esq": -1,
    "Dir": 1,
}

RESTRICOES = {
    "Esq": [0, 3, 6],  # Espaço vazio na coluna 0 não pode mover para esquerda
    "Dir":  [2, 5, 8],  # Espaço vazio na coluna 2 não pode mover para direita
}

def gera_sucessores(tabuleiro):
    """Gera os estados sucessores a partir do estado atual do tabuleiro."""
    
    zero_pos = tabuleiro.index(0)
    sucessores = []
    
    for move, delta in MOVES.items():
        nova_pos = zero_pos + delta
        
        # Verifica se o movimento é válido
        if 0 <= nova_pos < 9 and zero_pos not in RESTRICOES.get(move, []):
            novo_tabuleiro = list(tabuleiro)
            novo_tabuleiro[zero_pos], novo_tabuleiro[nova_pos] = novo_tabuleiro[nova_pos], novo_tabuleiro[zero_pos]
            sucessores.append((tuple(novo_tabuleiro), move))
    
    return sucessores

#--------------------------------------------------------------------------------------------------------
# ALGORITMO A*
#--------------------------------------------------------------------------------------------------------

def a_estrela(tabuleiro_inicial, heuristica):
    """Implementação do algoritmo A* para resolver o Jogo dos 8 Números."""
    
    if not eh_resolvivel(tabuleiro_inicial):
        return None, 0, 0  # Não é possível resolver
    
    fila_prioridade = []
    heapq.heappush(fila_prioridade, (heuristica(tabuleiro_inicial), 0, tabuleiro_inicial, []))
    visitados = set()
    
    while fila_prioridade:
        _, custo, estado_atual, caminho = heapq.heappop(fila_prioridade)
        
        if estado_atual in visitados:
            continue
        
        visitados.add(estado_atual)
        
        if estado_atual == OBJETIVO:
            return caminho, custo, len(visitados)  # Solução encontrada
        
        for sucessor, movimento in gera_sucessores(estado_atual):
            if sucessor not in visitados:
                novo_custo = custo + 1
                heapq.heappush(fila_prioridade, (novo_custo + heuristica(sucessor), novo_custo, sucessor, caminho + [movimento]))
    
    return None, 0, len(visitados)  # Sem solução encontrada

#--------------------------------------------------------------------------------------------------------
# MAIN
#--------------------------------------------------------------------------------------------------------

def ler_tabuleiro_inicial():
    """Lê o estado inicial do tabuleiro a partir da entrada do usuário."""

    print("-" * 50)
    print("     8 PUZZLE - RESOLUÇÃO COM A*")
    print("-" * 50)
    print("\nInsira o estado inicial do tabuleiro.")
    print("Use números de 0 a 8, separados por espaço.")
    print("O 0 representa o espaço vazio.")
    print("Exemplo: 1 2 5 3 4 0 6 7 8\n")

    while True:
        entrada = input("Estado inicial: ").strip()
        try:
            numeros = tuple(int(x) for x in entrada.split())
            if len(numeros) != 9:
                print("Erro: insira exatamente 9 números.")
                continue
            if sorted(numeros) != list(range(9)):
                print("Erro: use os números de 0 a 8, cada um exatamente uma vez.")
                continue
            return numeros
        except ValueError:
            print("Erro: entrada inválida. Use apenas números inteiros.")

def executa(estado_incial, heuristica, nome_heuristica):
    """Executa o algoritmo A* e exibe os resultados."""
    
    print(f"\n{'-' * 50}")
    print(f"    Heurística {nome_heuristica}")
    print(f"{'-' * 50}")
    
    inicio = time.time()
    caminho, custo, visitados = a_estrela(estado_incial, heuristica)
    fim = time.time()
    
    if caminho is not None:
        print(f"Solução encontrada: {' -> '.join(caminho)}")
        print(f"Custo da solução: {custo}")
    else:
        print("Nenhuma solução encontrada.")
    
    print(f"Número de estados visitados: {visitados}")
    print(f"Tempo de execução: {fim - inicio:.4f} segundos")

def main():
    estado_inicial = ler_tabuleiro_inicial()
    
    executa(estado_inicial, heuristica_manhattan, "Manhattan")
    executa(estado_inicial, heuristica_hamming, "Hamming")

    print("\n")

if __name__ == "__main__":
    main()