import numpy as np
from datetime import datetime

#função para gravar um log com exceções
def saveLog(text):

    #tenta
    try:

        #abrir o ficheiro log.txt para acrescentar 
        f = open("log.txt", "a")

        #escreve a mensagem desejada com a data e hora 
        f.write("\n" + text + '\t' + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "\n")

        #fecha o documento
        f.close()

        #retorna verdadeiro em conforme foi guardado o log
        return True

    #em caso de exceção
    except: 

        #retorna false em conforme não foi guardado o log
        return False

#função para ler de um ficheiro csv
def readFromFile(filename, dtype='float', delimiter=',', skiprows=1):

    #tenta
    try:

        #carrega o ficheiro
        raw = np.loadtxt(filename, dtype=dtype, delimiter=delimiter, skiprows=skiprows)
        #retorna como array
        return np.array(raw)

    #em caso de exceção por não existir o ficheiro
    except FileNotFoundError as fnfe:

        #grava a exceção no ficheiro log
        saveLog(str(fnfe))
        #imprime mensagem de erro
        print('\nFicheiro \"'+ filename +'\" não encontrado\n')
        #retorna um array vazio
        return np.array([])

    #em caso de exceção
    except Exception as e:
        
        #grava a exceção no ficheiro log
        saveLog(str(e))
        #imprime mensagem de erro
        print('\nErro ao ler ficheiro \"'+ filename +'\"\n')
        #retorna um array vazio
        return np.array([])