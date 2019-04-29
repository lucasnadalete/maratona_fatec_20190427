# Problema C - Corrida
nrc = int(input())
carros = {}
for i in range(nrc):
    id, tempo = [int(value) for value in input().split()]
    carros[id] = tempo
tp, qv = [int(value) for value in input().split()]
# Algoritmo para calcular
resultado = {}
distancia = tp * qv
for id in carros:
    resultado[id] = distancia // carros[id]
# Saida do algoritmo
output = '\n'.join([str(id) + ' ' + str(resultado[id]) for id in resultado])

print(output)
