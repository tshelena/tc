from random import getrandbits, randint, random, choice

def individual(nItens):
    """Cria um membro da populacao"""
    return [ getrandbits(1) for x in range(nItens) ]

def population(nIndividuos, nItens):
    """"Cria a populacao"""
    return [ individual(nItens) for x in range(nIndividuos) ]

def fitness(individuo, pesoMaximo, pesoEvalor):
    """Faz avaliacao do individuo"""
    pesoTotal, valorTotal = 0, 0
    for indice, valor in enumerate(individuo):
        pesoTotal += (individuo[indice] * pesoEvalor[indice][0])
        valorTotal += (individuo[indice] * pesoEvalor[indice][1])

    if (pesoMaximo - pesoTotal) < 0:
        return -1 
    #retorna -1 se a capacidade foi ultrapassada
    return valorTotal 
    #retorna o valor do indivíduo, em caso de indivíduo apto

def mediaFitness(populacao, pesoMaximo, pesoEvalor): 
    #utiliza apenas itens que não excedam a capacidade máxima
    """Encontra a avalicao media da populacao"""
    summed = sum(fitness(x, pesoMaximo, pesoEvalor) for x in populacao if fitness(x, pesoMaximo, pesoEvalor) >= 0)
    return summed / (len(populacao) * 1.0)

def selecaoRoleta(pais):
    """Seleciona um pai e uma mae baseado nas regras da roleta"""
    def sortear(fitnessTotal, indice_a_ignorar=-1): 
        # parametro garante que não vai selecionar o mesmo elemento
        """Monta roleta para realizar o sorteio"""
        roleta, acumulado, valorSorteado = [], 0, random()

        if indice_a_ignorar!=-1: 
        #desconta do total, o valor que sera retirado da roleta
            fitnessTotal -= valores[0][indice_a_ignorar]

        for indice, i in enumerate(valores[0]):
            if indice_a_ignorar==indice: 
        #ignora o valor ja utilizado na roleta
                continue
            acumulado += i
            roleta.append(acumulado/fitnessTotal)
            if roleta[-1] >= valorSorteado:
                return indice
    
    valores = list(zip(*pais)) 
        #cria 2 listas com os valores fitness e os cromossomos
    fitnessTotal = sum(valores[0])

    indicePai = sortear(fitnessTotal) 
    indiceMae = sortear(fitnessTotal, indicePai)

    pai = valores[1][indicePai]
    mae = valores[1][indiceMae]
    
    return pai, mae

def evolve(populacao, pesoMaximo, pesoEvalor, nCromossomos, mutate=0.05): 
    """Tabula cada individuo e o seu fitness"""
    pais = [ [fitness(x, pesoMaximo, pesoEvalor), x] for x in populacao if fitness(x, pesoMaximo, pesoEvalor) >= 0]
    pais.sort(reverse=True)
    
    # reproducao
    filhos = []
    while len(filhos) < nCromossomos:
        homem, mulher = selecaoRoleta(pais)
        meio = len(homem) // 2
        filho = homem[:meio] + mulher[meio:]
        filhos.append(filho)
    
    # mutacao
    for individuo in filhos:
        if mutate > random():
            pos_to_mutate = randint(0, len(individuo)-1)
            if individuo[pos_to_mutate] == 1:
                individuo[pos_to_mutate] = 0
            else:
                individuo[pos_to_mutate] = 1

    return filhos

