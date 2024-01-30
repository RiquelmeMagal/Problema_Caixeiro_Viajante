# solver.py

import gurobipy as gp

def resolver_problema(mat_custos, qtd_pontos):
    # Índices dos pontos de origem e destino
    origens = [i + 1 for i in range(qtd_pontos)]
    destinos = [i + 1 for i in range(qtd_pontos)]

    # Dicionário dos custos
    custos = dict()
    for i, origem in enumerate(origens):
        for j, destino in enumerate(destinos):
            custos[origem, destino] = mat_custos[i][j]

    # Inicializa o modelo
    m = gp.Model()

    # Variáveis de decisão
    x = m.addVars(origens, destinos, vtype=gp.GRB.BINARY)
    u = m.addVars(origens[1:], vtype=gp.GRB.INTEGER, ub=qtd_pontos - 1)

    # Função Objetivo
    m.setObjective(x.prod(custos), sense=gp.GRB.MINIMIZE)

    # Restrições que garantem que cada ponto será origem exatamente uma vez
    c1 = m.addConstrs(
        gp.quicksum(x[i, j] for j in destinos if i != j) == 1
        for i in origens)

    # Restrições que garantem que cada ponto será destino exatamente uma vez
    c2 = m.addConstrs(
        gp.quicksum(x[i, j] for i in origens if i != j) == 1
        for j in destinos)

    # Restrições de eliminação de subrotas
    c3 = m.addConstrs(
        u[i] - u[j] + qtd_pontos * x[i, j] <= qtd_pontos - 1
        for i in origens[1:] for j in destinos[1:] if i != j)

    # Executa o modelo
    m.optimize()

    # Constrói o vetor com o circuito
    circuito = [1]
    anterior = 1
    for ponto in range(qtd_pontos):
        for j in destinos:
            if round(x[anterior, j].X) == 1:
                circuito.append(j)
                anterior = j
                break

    # Imprime o circuito
    print("Circuito percorrido: ")
    print(circuito)
