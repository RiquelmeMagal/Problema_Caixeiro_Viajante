# Problema do caixeiro viajante
## Descrição
### O que é o problema?
O Problema do Caixeiro Viajante(*Traveling Salesman Problem* - TSP) consiste em encontrar a rota mais curta que um viajante deve percorrer para visitar um conjunto de cidades uma vez e retornar ao ponto de origem. O objetivo é minimizar a distância total percorrida, levando em consideração as distâncias entre todas as cidades. O problema é conhecido por ser NP-Completo, o que significa que não há algoritmo eficiente conhecido para resolvê-lo em tempo polinomial para um grande número de cidades. 

### O que é este projeto?

### Modelando a solução
Para resolver precisamos de uma base de dados com todos os pontos de origem, todos os pontos de destino e os custos para percorrer cada aresta. Como esse grafo é um circuíto, toda origem também é um destino, logo, só precisamos de uma variável `n` com a quantidade de vértices, representando o número de cidades, e a matriz com os custos para percorrer as arestas.

Também precisamos estar atentos a algumas restrições:
1. Cada ponto precisa ser origem ou destino exatamente uma vez.
2. Garantir que sub-circuitos sejam eliminados. Se considerarmos apenas a primeira restrição, grafos com subcircuitos que não se conectam entre si poderiam ser considerados.

Existem várias outras, entretanto, como vamos usar base de dados pequenas, para manter essa solução simples, consideraremos apenas essas.

#### As bases de dados
Existem várias bases de dados com soluções já conhecidas para o TSP. Você pode baixar todas [aqui](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/tsp/). Para esse projeto, selecionamos as seguintes:
| Base de dados | Número de cidades | Solução padrão |
|---|---|---|
| att48 | 48 | 10628 | 
| dantzig42 | 42 | 699 |
| fri26 | 26 | 937 |
| gr17 | 17 | 2085 |
| p01 | 15 | 291 |

#### A estrutura do projeto
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
## Instalação
## Como usar
## Licença
## Desenvolvedores
## Hardware e software sugeridos
