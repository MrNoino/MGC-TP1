import pandas as pd
import matplotlib.pyplot as plt
import utils

# função responsavel por ler um ficheiro csv e retornar em dataframe
def readCSV(filename):

    # tenta 
    try:

        # ler o ficheiro
        df = pd.read_csv(filename, index_col=False)

        # retornar dataframe
        return df

    #em caso de exceção por não existir o ficheiro
    except FileNotFoundError as fnfe:

        #grava a exceção no ficheiro log
        utils.saveLog(str(fnfe))
        #imprime mensagem de erro
        print('\nFicheiro \"'+ filename +'\" não encontrado\n')
        #retorna um dataframe vazio
        return pd.DataFrame()

    #em caso de exceção
    except Exception as e:
        
        #grava a exceção no ficheiro log
        utils.saveLog(str(e))
        #imprime mensagem de erro
        print('\nErro ao ler ficheiro \"'+ filename +'\"\n')
        #retorna um dataframe vazio
        return pd.DataFrame()

# função para contar o número de valores em falta no dataframe
def countMissingValues(dataframe):

    # dataframe.isnull(): retorna os valores em falta no dataframe | .sum(): retorna o somatório de todas as colunas | .sum(): retorna o somatório de todas as linhas
    return dataframe.isnull().sum().sum()
    
# função que remove as linhas com valores em falta do dataframe
def removeMissingValuesRows(dataframe):

    # remove as linhas com valores em falta do dataframe
    dataframe = dataframe.dropna()

    # repõe o index do dataframe e retorna
    return dataframe.reset_index(drop=True)

# função que calcula e retorna a estatistica descritiva de um dataframe
def descritiveStatistic(dataframe):

    # remove as linhas com valores em falta do dataframe
    dataframe = removeMissingValuesRows(dataframe= dataframe)

    # retorna a estatistica descritiva de um dataframe
    return dataframe.describe(include='all')

# função que desenha um gráfico 2D com base nos dados de um dataframe
def plot2D(dataframe):

    # remove as linhas com valores em falta do dataframe
    dataframe = removeMissingValuesRows(dataframe= dataframe)

    # array para definir a cor de cada ponto
    colors = []

    # array para definir o tamanho de cada ponto
    sizes = []

    # para cada linha do dataframe
    for l in range(len(dataframe)):

        # se a profundidade for menor que 10
        if float(dataframe.loc[l, 'depth']) < 10:

            # adiciona amarelo a cor do ponto
            colors.append('yellow')

        # se a profundidade for maior ou igual que 10 e menor que 50
        elif float(dataframe.loc[l, 'depth']) >= 10 and float(dataframe.loc[l, 'depth']) < 50:

            # adiciona vermelho a cor do ponto
            colors.append('red')

        # se não
        else:

            # adiciona azul a cor do ponto
            colors.append('blue')

        # adiciona ao tamanho do ponto o quadrado da magnitude
        sizes.append(float(dataframe.loc[l, 'mag']) **2)

    # atribui à coluna color os respetivos valores
    dataframe['color'] = colors

    # atribui à coluna size os respetivos valores
    dataframe['size'] = sizes

    # cria o gráfico com os dados do dataframe
    dataframe.plot(x= 'longitude', y= 'latitude', kind = 'scatter', c= 'color', s= 'size', title= 'Terramotos no Mundo')

    # mostra o gráfico
    plt.show()