from ga import *
# peso,valor
pesoEvalor = [[5, 40], [9, 20], 
              [8, 30], [15, 65], 
              [3, 20], [70, 300], 
              [5, 200], [22, 60], 
              [90, 300], [7, 200]]
pesoMaximo = 150
nCromossomos = 150
geracoes = 50
nItens = len(pesoEvalor) 

# execução do algoritmo
populacao = population(nCromossomos, nItens)
historicoFitness = [mediaFitness(populacao, pesoMaximo, pesoEvalor)]
for i in range(geracoes):
    populacao = evolve(populacao, pesoMaximo, pesoEvalor, nCromossomos)
    historicoFitness.append(mediaFitness(populacao, pesoMaximo, pesoEvalor))

# imprimir os resultados da execução
for indice,dados in enumerate(historicoFitness):
   print ("Geracao: ", indice," | Media de valor na mochila: ", dados)

print("\nPeso máximo:",pesoMaximo,"g\n\nItens disponíveis:")
for indice,i in enumerate(pesoEvalor):
    print("Item ",indice+1,": ",i[0],"g | R$",i[1])
    
print("\nExemplos de boas solucoes: ")
for i in range(5):
    print(populacao[i])

# gerar os gráficos da execução
from matplotlib import pyplot as plt
plt.plot(range(len(historicoFitness)), historicoFitness)
plt.grid(True, zorder=0)
plt.title("Problema da mochila")
plt.xlabel("Geracao")
plt.ylabel("Valor medio da mochila")
plt.show()

