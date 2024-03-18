def prim(mat_custos):
    # número de vértices
    n = len(mat_custos)

    # conjunto para armazenar vértices que já estão na AGM
    agm_vertices = set()

    # lista para armazenar as arestas da AGM
    agm_arestas = []

    # adiciona o primeiro vértice à AGM para que comece a partir dele
    agm_vertices.add(0)

    while len(agm_vertices) < n:
        # encontra a aresta de custo mínimo que conecta um vértice na AGM a um vértice fora da AGM (por isso que é necessário adicionar o primeiro vértice à AGM antes de começar o loop)
        minimo = float("inf")
        minimo_aresta = None
        for u in agm_vertices:
            for v in range(n):
                if v not in agm_vertices and mat_custos[u][v] < minimo:
                    minimo = mat_custos[u][v]
                    minimo_aresta = (u, v)

        # adiciona a aresta mínima à AGM
        agm_arestas.append(minimo_aresta)
        # adiciona o vértice que não estava na AGM à AGM
        agm_vertices.add(minimo_aresta[1])

    print_agm(agm_arestas, mat_custos)


def print_agm(agm_arestas, mat_custos):
    for aresta in agm_arestas:
        print(
            aresta[0], "-", aresta[1], "( Custo:", mat_custos[aresta[0]][aresta[1]], ")"
        )

    print(
        f"Tamanho da MST: {sum(mat_custos[aresta[0]][aresta[1]] for aresta in agm_arestas)}"
    )
