import numpy as np
import matplotlib.pyplot as plt
import part1

# função que desenha o gráfico 2D do exercicio a) da parte II
def plotA(population, rate, harvest, years, title, axisLabels, lineColor):

    #define 50 valores inteiros igualmente espaçados entre 1 e o número de anos definidos
    x = np.linspace(1, years, years)

    # cria array vazio
    y = np.array([])

    #calcula o crescimento de peixe no total de anos definido
    for year in x:

        # adiciona ao array a população calculada para o intervalo de anos 
        y = np.append(y, part1.pond(population, rate, harvest, year))

    # chama a função responsavel por desenhar o gráfico
    plot2D(x= x, y= y, lineColor= lineColor, title= title, axisLabels= axisLabels)

# função que desenha o gráfico 2D do exercicio b) da parte II
def plotB(population, rate, harvest, title, axisLabels, lineColor):

    # se a população inicial for inferior ou igual à população calculada após um ano então a população nunca será 0
    if population <= part1.pond(population=population, rate=rate, harvest=harvest):

        # mostra a mensagem ao utilizador
        print('\nO crescimento da população nunca irá ser 0\n')

        #para a execução da função
        return

    years = 1

    # calcula a população após um ano de crescimento
    finalPopulation = part1.pond(population=population, rate=rate, harvest=harvest, years=years)

    # cria um array vazio
    y = np.array([])

    # enquanto a população for maior que 0
    while finalPopulation > 0:

        # adiciona a população calculada ao array
        y = np.append(y, finalPopulation)

        # incrementa mais um ano 
        years += 1

        # calcula a população para o intervalo de anos
        finalPopulation = part1.pond(population=population, rate=rate, harvest=harvest, years=years)

    # retirar o último incremento
    years -= 1

    # imprime o número de anos 
    print('\nO número de anos até a população de peixe no lago ser 0 é de:', years, '\n')

    # cria um array com o tamanho de nr de anos com valores igualmente espaçados entre 1 e o nr de anos 
    x = np.linspace(1, years, years)

    # chama a função responsavel por desenhar o gráfico
    plot2D(x= x, y= y, lineColor= lineColor, title= title, axisLabels= axisLabels)


# função responsavel por desenhar o gráfico 2D
def plot2D(x, y, lineColor, title, axisLabels):

    #cria o gráfico 2D com os dados do crescimento ao longo dos anos
    ax = plt.plot(x, y, lineColor)

    #define o título para o gráfico
    plt.title(title)

    #define a etiqueta do eixo do x
    plt.xlabel(axisLabels[0])

    #define a etiqueta do eixo do y
    plt.ylabel(axisLabels[1])

    #mostra o gráfico
    plt.show()