import networkx as nx
import matplotlib.pyplot as plt
import utils

# função responsavel por criar o grafo
def graph(edges, type='directed'):

    #se não existe arestas
    if edges.size == 0:

        #imprime mensagem
        print('\nSem dados para desenhar o grafo\n')
        #termina a função
        return False

    # se o tipo de grafo é "directed"
    if type.lower() == 'directed':

        # cria  um grafo direto
        G = nx.DiGraph()

    # se o tipo de grafo é "undirected"
    elif type.lower() == 'undirected':
        
        # cria  um grafo indireto
        G = nx.Graph()

    # senão
    else:

        # imprime mensagem de que o tipo é invalido
        print('\nTipo de grafo inválido\n')

        #retorna falso
        return False

    #adiciona os nós
    for edge in edges:

        G.add_nodes_from(edge)

    #adiciona as arestas
    G.add_edges_from(edges)

    #retorna o grafo
    return G


#função para desenhar o grafo
def drawGraph(G, title= None):

    #cria a figura e subgráficos
    fig, ax = plt.subplots()

    #cria o layout de acordo com o grafo
    layout = nx.shell_layout(G)

    #desenha o grafo
    nx.draw(G, ax=ax, pos=layout, with_labels=True)

    #se foi definido o título
    if title:

        #define o título no grafo
        ax.set_title(title)

    #mostra o grafo
    plt.show()

# função que retorna a matriz adjacente
def adjacencyMatrix(edges):

    # cria o grafo
    G = graph(edges= edges)

    # retorna a matriz adjacente
    return nx.adjacency_matrix(G).todense()

# função que retorna a informação básica de um grafo
def basicInfo(edges):

    # cria o grafo
    G = graph(edges= edges)

    # retorna a informação sobre o grafo
    return nx.info(G)

# função que calcula a média do grau dos nós
def averageDegree(edges):

    # cria o grafo
    G = graph(edges= edges)

    # somatório
    sum = 0

    # para cada nó
    for node in G.nodes:

        # soma ao somatório o grau do nó 
        sum += G.degree[node]

    # retorna o somatório a dividir pelo número de nós (média)
    return sum / G.number_of_nodes()

# função que retorna a densidade do grafo
def density(edges):

    # cria o grafo
    G = graph(edges= edges)

    # retorna a densidade do grafo
    return nx.density(G)

# função que verifica se o grafo é plano
def planarity(edges):

    # cria o grafo
    G = graph(edges= edges)

    #retorna se o grafo é plano ou não
    return nx.check_planarity(G)

# função que calcula e retorna o caminho mais curto entre 2 nós
def shortestPath(edges, start, end):

    # cria o grafo
    G = graph(edges= edges)

    # tenta
    try:

        # retornar o caminho mais curto entre start e end
        return nx.shortest_path(G, start, end, weight= 'weight')

    # caso não exista caminho possível 
    except nx.exception.NetworkXNoPath as e:

        # guarda a exceção no log
        utils.saveLog(str(e))

        # retorna a msg de erro
        return 'Sem caminho entre ' + start + ' e ' + end

# função que atualiza o peso do grafo e adiciona mais arestas
def updateWeightAddEdges(edges, weight, moreEdges):

    # cria o grafo
    G = graph(edges= edges)

    # para cada aresta
    for u, v in G.edges:

        # atribui o valor do peso à aresta
        G.edges[u, v]["weight"] = weight

    # adiciona as arestas
    G.add_edges_from(moreEdges)

    # desenha o grafo
    drawGraph(G)