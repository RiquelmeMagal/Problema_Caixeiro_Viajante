# main.py

import ast
from datasets import criar_matriz, salvar_matriz, ler_matriz_do_arquivo
#from solver import resolver_problema
#from prim import prim
from dijkstra import dijkstra

def menu():
    print("Escolha uma opção:")
    print("1 - gr17_d (17 cidades)")
    print("2 - att48_d (48 cidades)")
    print("3 - p01_d (15 cidades)")
    print("4 - dantzig42_d (42 cidades)")
    print("5 - fri26_d (26 cidades)")

# Exemplo de uso sem função
menu()
valor = int(input("Digite uma das opções desejadas: "))
match valor:
    case 1:
        valor, PONTOS = "datasets_/gr17_d.txt", 17
    case 2:
        valor, PONTOS = "datasets_/att48_d.txt", 48
    case 3:
        valor, PONTOS = "datasets_/p01_d.txt", 15
    case 4:
        valor, PONTOS = "datasets_/dantzig42_d.txt", 42
    case 5:
        valor, PONTOS = "datasets_/fri26_d.txt", 26
    case _:
        print("Opção inválida. Escolha entre 1, 2, 3, 4 ou 5.")

matrizes_list = criar_matriz(valor)
salvar_matriz(matrizes_list, "nova_matriz.txt")

# Nome do arquivo
nome_arquivo = 'nova_matriz.txt'

# Chama a função para ler a matriz do arquivo
# Parâmetros do problema
qtd_pontos = PONTOS
# Matriz de custos
mat_custos = ler_matriz_do_arquivo(nome_arquivo)

# Chama a função para resolver o problema
#resolver_problema(mat_custos, qtd_pontos)
#prim(mat_custos)
dijkstra(mat_custos)