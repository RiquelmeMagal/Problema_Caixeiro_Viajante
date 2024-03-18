
from Christofides.full import christofides as christofides_full
from Christofides.minimal import christofides as christofides_min

from datasets import criar_matriz, salvar_matriz

def ler_matriz_do_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            # Lê o conteúdo do arquivo
            linhas = arquivo.readlines()

            # Cria a matriz a partir das linhas do arquivo
            matriz = [list(map(int, linha.split())) for linha in linhas]

        return matriz
    except Exception as e:
        print(f"Erro ao ler matriz do arquivo: {e}")
        return None


datasets = {
    "p01": {
        "path": "datasets_/p01_d.txt",
        "cities": 15,
        "minimal_cost": 291
    },
    "gr17": {
        "path": "datasets_/gr17_d.txt",
        "cities": 17,
        "minimal_cost": 2085
    },
    "fri26": {
        "path": "datasets_/fri26_d.txt",
        "cities": 26,
        "minimal_cost": 937
    },
    "dantzig42": {
        "path": "datasets_/dantzig42_d.txt",
        "cities": 42,
        "minimal_cost": 699
    },
    "att48": {
        "path": "datasets_/att48_d.txt",
        "cities": 48,
        "minimal_cost": 33523
    }
}

def calculate_efficiency(media_custo, minimal_cost):
    eficiencia = ((media_custo - minimal_cost) / minimal_cost) * 100
    if eficiencia > 0:
        return "-{:.2f}%".format(abs(eficiencia))
    else:
        return "{:.2f}%".format(abs(eficiencia))

def analytics():
    print("EXECUCAO DO ALGORITMO COMPLETO DE CHISTOFIDES PARA O TSP")
    print("+-----------------+-------------------+-------------------------+-------------------------------------+-------------------+")
    print("| Dataset         | Número de cidades | Tamanho mínimo do tour  | Tamanho médio do tour (3 execuções) | Eficiência (%)    |")
    print("+-----------------+-------------------+-------------------------+-------------------------------------+-------------------+")

    for dataset, info in datasets.items():
        resultados = []
        caminhos = []

        nome_arquivo = info["path"]
        matrizes_list = criar_matriz(nome_arquivo)
        salvar_matriz(matrizes_list, "nova_matriz.txt")

        for i in range(3):
            matriz_custos = ler_matriz_do_arquivo(nome_arquivo)
            coast, path = christofides_full(matriz_custos)
            resultados.append(int(coast))
            caminhos.append(path)

        media_custo = sum(resultados) / 3
        eficiencia = calculate_efficiency(media_custo, info["minimal_cost"])

        print("| {:<15} | {:<17} | {:<23} | {:<35} | {:<17} |".format(dataset, info["cities"], info["minimal_cost"], int(media_custo), eficiencia))

    print("+-----------------+-------------------+-------------------------+-------------------------------------+-------------------+")

    print("EXECUCAO DO ALGORITMO SIMPLIFICADO DE CHISTOFIDES PARA O TSP")
    print("+-----------------+-------------------+-------------------------+-------------------------------------+-------------------+")
    print("| Dataset         | Número de cidades | Tamanho mínimo do tour  | Tamanho médio do tour (3 execuções) | Eficiência (%)    |")
    print("+-----------------+-------------------+-------------------------+-------------------------------------+-------------------+")

    for dataset, info in datasets.items():
        resultados = []
        caminhos = []

        nome_arquivo = info["path"]
        matrizes_list = criar_matriz(nome_arquivo)
        salvar_matriz(matrizes_list, "nova_matriz.txt")

        for i in range(3):
            matriz_custos = ler_matriz_do_arquivo(nome_arquivo)
            coast, path = christofides_min(matriz_custos)
            resultados.append(int(coast))
            caminhos.append(path)

        media_custo = sum(resultados) / 3
        eficiencia = calculate_efficiency(media_custo, info["minimal_cost"])

        print("| {:<15} | {:<17} | {:<23} | {:<35} | {:<17} |".format(dataset, info["cities"], info["minimal_cost"], int(media_custo), eficiencia))

    print("+-----------------+-------------------+-------------------------+-------------------------------------+-------------------+")

    
if __name__ == "__main__":
    analytics()
