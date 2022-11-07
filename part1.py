# exercício a)
# Pseudocódigo: para calcular a população do lago é necessário implementar a formula de crescimento, que é a seguinte
# população é igual à percentagem de crescimento anual vezes a população atual do lago 
# menos a pesca máxima anual mais a quantidade de peixe reposto anualmente 
# No caso de ser calculado ao longo de um número de anos, esta formula deve ser chamada 
# novamente com o calculo da população do ano anterior

#função recursiva que calcula o crescimento anual de peixe num lago ao longo de um número dado de anos
def pond(population = 12000, rate = 8, harvest = 1500, years = 1, restock = 0):
    #calcula o valor do crescimento da população no ano.
    population =  int((1+rate/100) * population - harvest + restock)

    #retira um ano
    years -= 1

    #se ja foi calculado o crescimento de peixe ao longo dos anos requiridos ou se a população é menor ou igual a 0
    if years == 0 or population <= 0:

        #retorna a população
        return population

    #senão
    else:
        
        #retorna a função, de modo a fazer a recursividade
        return pond(population, rate, harvest, years)

# função que verifica quantos anos são necessários para extinguir os peixes do lago
def diesOut(population = 12000, rate = 8, harvest = 1500):

    years = 1

    # calcula a população após um ano de crescimento 
    finalPopulation = pond(population=population, rate=rate, harvest=harvest, years=years)

    # se a população inicial for inferior ou igual à população calculada após um ano então a população nunca será 0
    if population <= finalPopulation:

        # mostra a mensagem ao utilizador
        print('\nO crescimento da população nunca irá ser 0\n')

        #retorna falso 
        return False

    # enquanto a população não for 0
    while finalPopulation > 0:

        #adiciona um ano
        years += 1

        #calcula a população para um intervalo de anos
        finalPopulation = pond(population=population, rate=rate, harvest=harvest, years=years)

    # retirar o último incremento
    years -= 1

    # retorna o número de anos até extinguir os peixes
    return years