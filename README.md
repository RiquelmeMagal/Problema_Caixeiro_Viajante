# Problema do caixeiro viajante
## Descrição
### ❓ O que é o problema?
O Problema do Caixeiro Viajante é um problema cujo objetivo é determinar a menor rota para percorrer uma série de cidades, visitando uma única vez cada uma delas, e retornar à cidade de origem. Este projeto tem como objetivo aplicar a teoria dos grafos para resolver o Problema do Caixeiro Viajante, sendo cada cidade representada por um nó e as conexões entre as cidades sendo as arestas.

### 🔨 Modelando a solução
Para resolver precisamos de uma base de dados com todos os pontos de origem, todos os pontos de destino e os custos para percorrer cada aresta. Como esse grafo é um circuíto, toda origem também é um destino, logo, só precisamos de uma variável `n` com a quantidade de vértices, representando o número de cidades, e a matriz com os custos para percorrer as arestas.

Também precisamos estar atentos a algumas restrições:
1. Cada ponto precisa ser origem ou destino exatamente uma vez.
2. Garantir que sub-circuitos sejam eliminados. Se considerarmos apenas a primeira restrição, grafos com subcircuitos que não se conectam entre si poderiam ser considerados.

Existem várias outras, entretanto, como vamos usar base de dados pequenas, para manter essa solução simples, consideraremos apenas essas.

### ❗IMPORTANTE:
Antes de começarmos, é importante destacar que o Gurobi impõe limitações na quantidade de dados que podem ser processados neste conjunto de dados. Ao executar o arquivo 'att48', você pode encontrar um erro que solicita a aquisição de uma licença completa. Caso você seja um estudante, é possível obter uma licença gratuita utilizando seu e-mail acadêmico.
Lembre-se das restrições das licenças: todo teste deve ser conduzido com o intuito de aprendizado, e não para propósitos comerciais. Recomendamos cautela ao realizar qualquer experimento.

#### 💾 As bases de dados
Existem várias bases de dados com soluções já conhecidas para o TSP. Você pode baixar todas [aqui](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/tsp/). Para esse projeto, selecionamos as seguintes:
| Base de dados | Número de cidades | Solução padrão |
|---|---|---|
| att48 | 48 | 33523 | 
| dantzig42 | 42 | 699 |
| fri26 | 26 | 937 |
| gr17 | 17 | 2085 |
| p01 | 15 | 291 |

#### 📑 A estrutura do projeto
```
datasets # pasta com os datasets que utilizaremos
| att48_d.txt
| dantzig42_d.txt
| fri26_d.txt
| gr17_d.txt
| p01_d.txt
datasets.py # arquivo com as funções responsáveis por ler os datasets e transformá-los em matriz
main.py # arquivo central do projeto com o menu de seleção e a chamada das funções
solver.py # algorítmo para solução do problema
requeriments.txt # dependências do projeto
.gitignore
README.md
LICENSE 
```

1. O programa começa no arquivo `main.py` que inicia oferecendo ao usuário um menu para seleção da base de dados:
   ```
   def menu():
    print("Escolha uma opção:")
    print("1 - gr17_d (17 cidades)")
    print("2 - att48_d (48 cidades)")
    print("3 - p01_d (15 cidades)")
    print("4 - dantzig42_d (42 cidades)")
    print("5 - fri26_d (26 cidades)")
   ```
2. A partir do que ele selecionar, ele chama as funções para ler a base de dados, gerar uma matriz de custos e salvar em um novo arquivo:
   ```
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
      nome_arquivo = 'nova_matriz.txt'
      qtd_pontos = PONTOS
      mat_custos = ler_matriz_do_arquivo(nome_arquivo)
   ```
3. Em seguida ele chama a função para resolver o problema:
   ```
    resolver_problema(mat_custos, qtd_pontos)
   ```
Para resolver o problema, usamos a biblioteca `gurobi`. No arquivo `solver.py`, a partir dos parâmetros passados para a função temos:
1. Gera uma lista com todos os pontos de origem e destino:
   ```
   origens = [i + 1 for i in range(qtd_pontos)]
   destinos = [i + 1 for i in range(qtd_pontos)]
   ```
2. Transforma a matriz de custos em um dicionário
   ```
   custos = dict()
    for i, origem in enumerate(origens):
        for j, destino in enumerate(destinos):
            custos[origem, destino] = mat_custos[i][j
   ```
3. Inicializa o modelo, cria as variáveis de decisão e define a função objetivo
   ```
    m = gp.Model()

    x = m.addVars(origens, destinos, vtype=gp.GRB.BINARY)
    u = m.addVars(origens[1:], vtype=gp.GRB.INTEGER, ub=qtd_pontos - 1)

    m.setObjective(x.prod(custos), sense=gp.GRB.MINIMIZE)
   ```
4. Adiciona as restrições ao modelo
   ```
    c1 = m.addConstrs(
        gp.quicksum(x[i, j] for j in destinos if i != j) == 1
        for i in origens)

    c2 = m.addConstrs(
        gp.quicksum(x[i, j] for i in origens if i != j) == 1
        for j in destinos)

    c3 = m.addConstrs(
        u[i] - u[j] + qtd_pontos * x[i, j] <= qtd_pontos - 1
        for i in origens[1:] for j in destinos[1:] if i != j)
    ```
5. Executa o algorítmo, gera um vetor com o circuito e imprime isso no console:
   ```
    m.optimize()

    circuito = [1]
    anterior = 1
    for ponto in range(qtd_pontos):
        for j in destinos:
            if round(x[anterior, j].X) == 1:
                circuito.append(j)
                anterior = j
                break

    print("Circuito percorrido: ")
    print(circuito)
   ```
   
## 💻 Como rodar o projeto na sua máquina
> Hardware sugerido: Processador 3.9GHz Intel Core i7 com 16Gb de RAM e sistema operacional Linux.
> Hadware sugerido: Processador 4.4Ghz Intel Core i5 com 16Gb de RAM e sistema operacional Linux. (Ubuntu 22.04 LTS)

#### 💻 Clone do projeto 
Com o git instalado na sua máquina, clone o repositório:
```
https://github.com/RiquelmeMagal/Problema_Caixeiro_Viajante.git
```
#### 🔖 Instação das dependências
Dentro da pasta do projeto, instale as dependências com o comando:
```
pip install -r requirements.txt
```
Depois disso, é só executar o programa e interagir com o menu.

## 📜 Licença
- [GNU 3.0](https://github.com/RiquelmeMagal/Problema_Caixeiro_Viajante/blob/main/LICENSE)

## Desenvolvedores
| Nome | E-mail |
| --- | --- |
| Gustavo Henrique | [gustavo.malaquias@arapiraca.ufal.br](mailto:gustavo.malaquias@arapiraca.ufal.br) |
| Riquelme Magalhães | [riquelme.souza@arapiraca.ufal.br](mailto:riquelme.souza@arapiraca.ufal.br) |
| Alex Sandro | [alex.oliveira@arapiraca.ufal.br](mailto:alex.oliveira@arapiraca.ufal.br) |
| Jaiane Oliveira | [jaiane.oliveira@arapiraca.ufal.br](mailto:jaiane.oliveira@arapiraca.ufal.br) |

