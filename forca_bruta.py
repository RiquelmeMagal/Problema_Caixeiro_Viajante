import itertools
import sys

# Função auxiliar para calcular o custo total de uma rota
def calcular_custo_total(rota, mat_custos):
    custo_total = 0
    n = len(rota)
    for i in range(n - 1):
        origem, destino = rota[i], rota[i + 1]
        custo_total += mat_custos[origem][destino]
    custo_total += mat_custos[rota[-1]][rota[0]]  # Adiciona o custo de volta ao ponto de partida
    return custo_total

# Função de força bruta para resolver o problema do caixeiro viajante
def forca_bruta(mat_custos):
    n = len(mat_custos)
    menor_custo = sys.maxsize
    melhor_rota = None

    # Gerar todas as permutações dos vértices
    for rota in itertools.permutations(range(n)):
        custo_total = calcular_custo_total(rota, mat_custos)

        # Atualiza o menor custo e a melhor rota, se necessário
        if custo_total < menor_custo:
            menor_custo = custo_total
            melhor_rota = rota

    return menor_custo, melhor_rota
