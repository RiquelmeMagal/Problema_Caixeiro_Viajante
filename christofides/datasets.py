# datasets.py
import ast

def criar_matriz(dataset: str):
    try:
        # Código para criar a matriz a partir do arquivo
        with open(dataset, "r") as file:
            content = file.readlines()

        # Remove espaços em branco e quebras de linha
        content = [line.strip() for line in content]

        # Cria a matriz a partir do conteúdo do arquivo
        matrix = [list(map(int, line.split())) for line in content]

        # Lista de matrizes
        matrices_list = [matrix]  # Adicione quantas matrizes você precisar

        return matrices_list
    except FileNotFoundError as Error:
        print(f"Arquivo não encontrado {Error}")

def salvar_matriz(matrices_list, nome_arquivo):
    try:
        # Salva a lista de matrizes em um novo arquivo
        with open(nome_arquivo, "w") as new_file:
            for matrices in matrices_list:
                new_file.write(str(matrices) + "\n")
        # print("Sucesso em criar o arquivo.")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")

def ler_matriz_do_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        # Lê o conteúdo do arquivo
        conteudo = arquivo.read()

        # Usa ast.literal_eval para analisar a string de forma segura
        matriz = ast.literal_eval(conteudo)

    return matriz
