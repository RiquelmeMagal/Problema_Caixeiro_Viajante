import sys

#Implementa o dijkstra para o PCV
def dijkstra(mat_custos):
    numero_de_cidades = len(mat_custos)
    cidades_visitadas = [False] * numero_de_cidades
    cidades_visitadas[0] = True
    
    posição_atual = 0
    quantidade = 1
    custo = 0
    ciclo_hamiltoniano = sys.maxsize

    resultado_do_pcv = procurar_ciclo_hamiltoniano(mat_custos, cidades_visitadas, posição_atual, numero_de_cidades, quantidade, custo, ciclo_hamiltoniano)

    print(f"Distância total: {resultado_do_pcv}")

#Método auxiliar para encontrar o ciclo hamiltoniano ponderado mínimo
def procurar_ciclo_hamiltoniano(mat_custos, cidades_visitadas, posição_atual, numero_de_cidades, quantidade, custo, ciclo_hamiltoniano):
    if quantidade == numero_de_cidades and mat_custos[posição_atual][0] > 0:
        ciclo_hamiltoniano = min(ciclo_hamiltoniano, custo + mat_custos[posição_atual][0])
        return ciclo_hamiltoniano

    for i in range(numero_de_cidades):
        if not cidades_visitadas[i] and mat_custos[posição_atual][i] > 0:
            cidades_visitadas[i] = True
            ciclo_hamiltoniano = procurar_ciclo_hamiltoniano(mat_custos, cidades_visitadas, i, numero_de_cidades, quantidade + 1, custo + mat_custos[posição_atual][i], ciclo_hamiltoniano)
            cidades_visitadas[i] = False
    return ciclo_hamiltoniano
