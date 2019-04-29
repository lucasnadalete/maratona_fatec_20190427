# Problema E - Bilhar
# dAB = (x2 - x1)2 + (y2 - y1)2 raiz quadrada deste resultado

qb = int(input())
distancia = 0.0

x0, y0 = [float(value) for value in input().split()]
x1, y1 = x0, y0
# Calcula a distancia entre os pontos
for i in range((qb - 1)):
    x2, y2 = [float(value) for value in input().split()]
    distancia += (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5
    x1, y1 = x2, y2
# Calcula a distancia entre o fechamento dos pontos
x2, y2 = x0, y0
distancia += (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5

print('%.2f' %distancia)