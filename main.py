# main.py

import ast
from datasets import criar_matriz, salvar_matriz, ler_matriz_do_arquivo
from prim import prim
from dijkstra import dijkstra
from forca_bruta import forca_bruta

def menu():
    print("Escolha uma opção:")
    print("1 - gr17_d (17 cidades)")
    print("2 - att48_d (48 cidades)")
    print("3 - p01_d (15 cidades)")
    print("4 - dantzig42_d (42 cidades)")
    print("5 - fri26_d (26 cidades)")

def resolver_problema(mat_custos, qtd_pontos, escolha_algoritmo):
    if escolha_algoritmo == 1:
        print("Utilizando algoritmo de Prim:")
        prim(mat_custos)
    elif escolha_algoritmo == 2:
        print("Utilizando algoritmo de Dijkstra:")
        dijkstra(mat_custos)
    elif escolha_algoritmo == 3:
        print("Utilizando algoritmo de força bruta:")
        melhor_custo, melhor_rota = forca_bruta(mat_custos)
        print("Melhor rota:", melhor_rota)
        print("Menor custo:", melhor_custo)
    else:
        print("Opção inválida. Escolha entre 1, 2 ou 3.")

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

# Escolha do algoritmo
escolha_algoritmo = int(input("Escolha o algoritmo (1 - Prim, 2 - Dijkstra, 3 - Força Bruta): "))

# Chama a função para resolver o problema
resolver_problema(mat_custos, qtd_pontos, escolha_algoritmo)
