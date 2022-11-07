import part1, part2, part3, part4, part5
import utils

# opção igual a '1' para não parar na condição do ciclo
option = '1';

#enquanto a opção não for '0'
while(option != '0'):

    #Apresenta o menu ao utilizador
    option = input('\tMenu\n\nPARTE V\n19. c) d) e) Gráfico 2D\n18. b) Calcular as estatística descritiva dos dados\n17. a) Contar o número de valores em falta e remover as linhas com valores em falta\n\nPARTE IV\n16. h) Atualizar o peso e adicionar mais arestas ao grafo\n15. g) Calcular o caminho mais curto para os nós definidos pelo utilizador14. f) Calcular a planaridade e a matriz adjacente\n13. e) Densidade do grafo\n12. d) Calcula o angúlo médio do grafo\n11. c) Calcula o número de nós e arestas\n10. b) Imprime a matriz adjacente\n9. a) Desenha um grafo com dados do ficheiro\n\nPARTE III\n8. Desenhar gráfico 3D a partir do ficheiro data.csv\n\nPARTE II\n7. b) Desenhar um gráfico 2D com a evolução da população de peixe até que seja 0\n6. a) Desenhar um gráfico 2D com a evolução da população após uma quantidade de anos\n\nPARTE I\n5. f) Função pond com o crescimento anual e restock de peixe anual\n4. e) Calcular a quantidade de peixes após 15 anos e com máximo de pesca de 800\n3. d) A pesca máxima é sustentável? Se não, em quanto tempo se extingue? Deve-se reduzir o valor da pesca máxima? Para quanto?\n2. c) Imprimir a população apôs 10 anos\n1. b) Retornar população após um número de anos\n0. Sair\nOpção: ')

    #se opção igual a '1'
    if option == '1':

        # tenta
        try:

            # pede o número de anos ao utilizador
            years = int(input('\nNúmero de anos em estudo: '))

            # calcula a população para o nr de anos forrnecido
            population = part1.pond(years= years)

            # imprime os valores
            print("\nTotal de peixes ao fim de", years, "anos é de:", population, "\n") 

        # caso o valor introduzido não tenha sido o esperado
        except ValueError as e:

            # imprime msg de erro
            print('\nValor inválido, tente novamente.\n')

            # escreve um log com a exceção
            utils.saveLog(str(e))

        # caso exista uma exceção 
        except Exception as e:

            # imprime uma msg de erro
            print('\nAlgo correu mal, tente novamente.\n')

            # escreve um log com a exceção
            utils.saveLog(str(e))        

    #se opção igual a '2'
    elif option == '2':

        # calcula a população ao fim de 10 anos
        population = part1.pond(years= 10)

        # imprime os valores
        print("\nTotal de peixes ao fim de 10 anos é de:", population, "\n")

    #se opção igual a '3'
    elif option == '3':

        # imprime os valores e a sua interpretação
        print('\nEste valor é da população no lago ao longo de um ano:', part1.pond(),
        '\nEste é número de anos até a população de peixes seja 0:', part1.diesOut(),
        '\nSe repararmos, o total de população apôs um ano é inferior à população inicial, então em algum momento, com a taxa de crescimento de 8% e a pesca máxima de 1500, a população do lago será 0.',
        '\nPara não deixar a população de peixe no lago extinguir, devemos definir um valor de pesca máximo inferior ou igual ao crescimento. No caso de a população inicial ser 12000 e o crescimento de 8% anual, então a pesca máxima anual não deverá ser superior a 960 que é o crescimento anual.',
        '\nSe ao invés de ter 1500 como pesca máxima anual, tivermos 960, então a população nunca será diferente de 12000 como mostra a função: ', part1.pond(harvest=960),
        '\n')

    #se opção igual a '4'
    elif option == '4':

        # calcula a população com população inicial de 12000, pesca anual de 800 ao fim de 15 anos
        population = part1.pond(population= 12000, harvest= 800, years= 15)

        # imprime os valores
        print("\nTotal de peixes ao fim de 15 anos é de:", population, "\n")

    #se opção igual a '5'
    elif option == '5':

        # calcula a população com população inicial de 12000 peixes, pesca anual de 800 e reposição anual de 1000 peixes ao fim de 15 anos
        population = part1.pond(population= 12000, rate= 8, harvest= 800, years= 15, restock= 1000)

        # imprime os valores
        print("\nTotal de peixes ao fim de 15 anos é de:", population, "\n")

    #se opção igual a '6'
    elif option == '6':

        # tenta
        try:

            # pede o número de peixes inicial
            population = int(input('\nPopulação de peixe: '))

            # pede o crescimento anual
            rate = float(input('\nTaxa de crescimento da população (em %): '))

            # pede a pesca máxima anual
            harvest = int(input('\nMáximo de pesca anual: '))

            # pede o nr de anos em estudo
            years = int(input('\nNúmero de anos em estudo: '))

            # pede o título do gráfico
            title = input('\nTítulo do gráfico: ')

            # array para guardar as etiquetas dos eixos
            axisLabels = []

            # pede a etiqueta do eixo x
            axisLabels.append(input('\nEtiqueta do eixo x: '))

            # pede a etiqueta do eixo y
            axisLabels.append(input('\nEtiqueta do eixo y: '))

            # pede a cor da linha do gráfico
            lineColor = input('\nCor da linha do gráfico: ')

            # desenha o gráfico
            part2.plotA(population= population, rate= rate, harvest= harvest, years= years, title= title, axisLabels= axisLabels, lineColor= lineColor)

        # caso o valor introduzido não tenha sido o esperado
        except ValueError as e:

            # imprime msg de erro
            print('\nValor inválido, tente novamente.\n')

            # escreve um log com a exceção
            utils.saveLog(str(e))

        # caso ocorra uma exceção
        except Exception as e:

            # imprime msg de erro
            print('\nAlgo correu mal, tente novamente.\n')

            # escreve um log com a exceção
            utils.saveLog(str(e))

    #se opção igual a '7'
    elif option == '7':

        # tenta
        try:

            # pede a população inicial de peixes
            population = int(input('\nPopulação de peixe: '))

            # pede o crescimento anual
            rate = float(input('\nTaxa de crescimento da população (em %): '))

            # pede a pesca máxima anual
            harvest = int(input('\nMáximo de pesca anual: '))

            # pede o título do gráfico
            title = input('\nTítulo do gráfico: ')

            # array para guardar as etiquetas dos eixos
            axisLabels = []

            # pede a etiqueta do eixo do x
            axisLabels.append(input('\nEtiqueta do eixo x: '))

            # pede a etiqueta do eixo do y
            axisLabels.append(input('\nEtiqueta do eixo y: '))

            # pede a cor da linha do gráfico
            lineColor = input('\nCor da linha do gráfico: ')

            # desenha o gráfico
            part2.plotB(population= population, rate= rate, harvest= harvest, title= title, axisLabels= axisLabels, lineColor= lineColor)

        # caso o valor introduzido não tenha sido o esperado
        except ValueError as e:

            # imprime a msg de erro
            print('\nValor inválido, tente novamente.\n')

            # escreve um log com a exceção
            utils.saveLog(str(e))

        # caso ocorra uma exceção
        except Exception as e:

            # imprime a msg de erro
            print('\nAlgo correu mal, tente novamente.\n')

            # escreve um log com a exceção
            utils.saveLog(str(e))

    #se opção igual a '8'
    elif option == '8':

        # desenha um gráfico 3D
        part3.plot3D(utils.readFromFile('data.csv'))

    #se opção igual a '9'
    elif option == '9':

        # pede o título do grafo
        title = input('\nTítulo do grafo: ')

        # pede o tipo de grafo
        type = input('\nTipo de grafo (directed ou undirected): ')

        # cria o grafo
        G = part4.graph(utils.readFromFile('graph.txt', 'str', ' ', 0), type= type)

        # se o grafo foi criado
        if(G):

            # desenha o grafo
            part4.drawGraph(G= part4.graph(utils.readFromFile('graph.txt', 'str', ' ', 0), type= type), title= title)

    #se opção igual a '10'
    elif option == '10':

        # imprime a matriz adjacente
        print('\nMatriz adjacente:\n' + str(part4.adjacencyMatrix(edges= utils.readFromFile(filename= 'graph.txt', dtype= 'str', delimiter=' ', skiprows= 0))), '\n')

    #se opção igual a '11'
    elif option == '11':

        # imprime a informação básica do grafo
        print('\nInformação básica do Grafo:\n' + str(part4.basicInfo(edges= utils.readFromFile(filename= 'graph.txt', dtype= 'str', delimiter=' ', skiprows= 0))), '\n')

    #se opção igual a '12'
    elif option == '12':

        # imprime o angulo médio dos nós do grafo
        print('\nO ângulo médio é de:', part4.averageDegree(edges= utils.readFromFile(filename= 'graph.txt', dtype= 'str', delimiter=' ', skiprows= 0)), '\n')

    #se opção igual a '13'
    elif option == '13':

        # imprime a densidade do grafo
        print('\nA densidade do grafo é:', part4.density(edges= utils.readFromFile(filename= 'graph.txt', dtype= 'str', delimiter=' ', skiprows= 0)), '\n')

    #se opção igual a '14'
    elif option == '14':
    
        # imprime se o grafo é plano ou não
        print('\nO grafo' + (' não' if not part4.planarity(edges= utils.readFromFile(filename= 'graph.txt', dtype= 'str', delimiter=' ', skiprows= 0)) else '') + ' é plano\n')

    #se opção igual a '15'
    elif option == '15':

        # pede o primeiro nó
        start = input('\nPrimeiro nó: ')
        # pede o último nó 
        end = input('\nÚltimo nó: ')

        # imprime o cvaminho mais curto entre o primeiro e último nó
        print('\nO caminho mais curto é:\n' + str(part4.shortestPath(edges= utils.readFromFile(filename= 'graph.txt', dtype= 'str', delimiter=' ', skiprows= 0), start= start, end= end)), '\n')

    #se opção igual a '16'
    elif option == '16':
        
        # tenta
        try:

            # pede o peso do grafo
            weight = int(input('\nPeso dos nós: '))

            # nó 1
            node1 = ''

            # nó 2
            node2 = ''

            # array para armazenar mais arestas
            moreEdges = []

            # enquanto nó 1 e nó 2 diferente de 'sair'
            while node1.lower() != 'sair' and node2.lower() != 'sair':

                # pede o nó 1
                node1 = input('\nInsira o primeiro nó da aresta (escreva "sair" para parar): ')

                # se nó 1 igual a 'sair'
                if node1.lower() == 'sair':

                    # termina o ciclo
                    break;

                # pede o nó 1
                node2 = input('\nInsira o segundo nó da aresta (escreva "sair" para parar): ')

                # se nó 2 igual a 'sair'
                if node2.lower() == 'sair':

                    # termina o ciclo
                    break

                # adiciona a aresta ao array
                moreEdges.append([node1, node2])

            # atualiza o peso do grafo, adiciona mais arestas e desenha o grafo
            part4.updateWeightAddEdges(edges= utils.readFromFile(filename= 'graph.txt', dtype= 'str', delimiter=' ', skiprows= 0), weight= weight, moreEdges= moreEdges)

        # caso o valor introduzido não seja o esperado
        except ValueError as e:

            # imprime msg de erro
            print('\nValor inválido, tente novamente.\n')

            # escreve um log com a exceção
            utils.saveLog(str(e))

        # caso ocorra uma exceção
        except Exception as e:

            # imprime msg de erro
            print('\nAlgo correu mal, tente novamente.\n')

            # escreve um log com a exceção
            utils.saveLog(str(e))

    #se opção igual a '17'
    elif option == '17':

        # le e converte um ficheiro csv em data frame
        dataframe = part5.readCSV('all_month.csv')

        # imprime o dataframe
        print('\nO total de valores em falta são: ' + str(part5.countMissingValues(dataframe= dataframe)), '\nAo remover as linhas com os valores em falta, os dados são:\n\n' + str(part5.removeMissingValuesRows(dataframe= dataframe)))

    #se opção igual a '18'
    elif option == '18':

        # imprime a estatistica descritiva do data frame
        print('\nEstatística descritiva dos dados:\n\n' + str(part5.descritiveStatistic(part5.readCSV('all_month.csv'))), '\n')

    #se opção igual a '19'
    elif option == '19':

        # desenha um gráfico 2D a partir dos dados do ficheiro
        part5.plot2D(part5.readCSV('all_month.csv'))

    #se opção igual a '0'
    elif option == '0':

        # imprime msg de encerramento
        print('\nPrograma encerrado!\n')
        
    #se opção diferente de todas as outras opções a cima
    else:

        # imprime msg de erro
        print('\nOpção inválida, tente novamente\n')