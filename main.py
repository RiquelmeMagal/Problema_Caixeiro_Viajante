import gurobipy as gp
import ast

def menu():
    print("Escolha uma opção:")
    print("1 - gr17_d (17 cidades)")
    print("2 - att48_d (48 cidades)")
    print("3 - p01_d (15 cidades)")
    print("4 - dantzig42_d (42 cidades)")
    print("5 - fri26_d (26 cidades)")


def criarArquivo(dataset: str):
    try:
        # Lê o conteúdo do arquivo
        with open(dataset, "r") as file:
            content = file.readlines()

        # Remove espaços em branco e quebras de linha
        content = [line.strip() for line in content]

        # Cria a matriz a partir do conteúdo do arquivo
        matrix = [list(map(int, line.split())) for line in content]

        # Lista de matrizes
        matrices_list = [matrix]  # Adicione quantas matrizes você precisar

        # Salva a lista de matrizes em um novo arquivo
        with open("nova_matriz.txt", "w") as new_file:
            for matrices in matrices_list:
                new_file.write(str(matrices) + "\n")
        print("Sucesso em criar o arquivo.")
    except FileNotFoundError as Error:
        print(f"Arquivo não encontrado {Error}")


menu()
# Exemplo de uso sem função
valor = int(input("Digite uma das opções desejadas: "))
match valor:
    case 1:
        valor, PONTOS = "gr17_d.txt", 17
        criarArquivo(valor)
    case 2:
        valor, PONTOS = "att48_d.txt", 48
        criarArquivo(valor)
    case 3:
        valor, PONTOS = "p01_d.txt", 15
        criarArquivo(valor)
    case 4:
        valor, PONTOS = "dantzig42_d.txt", 42
        criarArquivo(valor)
    case 5:
        valor, PONTOS = "fri26_d.txt", 26
        criarArquivo(valor)
    case _:
        print("Opção inválida. Escolha entre 1, 2, 3, 4 ou 5.")


# Função para ler a matriz do arquivo
def ler_matriz_do_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        # Lê o conteúdo do arquivo
        conteudo = arquivo.read()

        # Usa ast.literal_eval para analisar a string de forma segura
        matriz = ast.literal_eval(conteudo)

    return matriz

# Nome do arquivo
nome_arquivo = 'nova_matriz.txt'

# Chama a função para ler a matriz do arquivo
# Parâmetros do problema
qtd_pontos = PONTOS
# Matriz de custos
mat_custos = ler_matriz_do_arquivo(nome_arquivo)




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