# Problema B - Bolsa Binaria

# Calculo da quantidade e lucros (recursivamente)
def calculate(modelos, compTd):
    q, v = modelos[0][0], modelos[0][1]
    qb = compTd // q
    lucro = qb * v
    if len(modelos) == 1:
        return (qb, lucro)
    else:
        qbS, lucroS = calculate(modelos[1:], compTd % q)
        return (qb + qbS), (lucro + lucroS)

# Geracao das combinacoes de modelos a serem processados
def backtracking(modelos, qtdeBv, compTd):
    cModelos = []
    lucros = []
    for i in range(3):
        cModelos.append(modelos[i])
        for j in range(3):
            if i != j:
                cModelos.append(modelos[j])
        qb, lucro = calculate(cModelos, compTd)
        if (qb >= qtdeBv):
            lucros.append(lucro)
        cModelos.clear()
    lucros.sort(reverse=True)
    return str(lucros[0]) if len(lucros) > 0 else 'IMPOSSIVEL'

# Processamento principal
modelos = []
compTd, qtdeBv = [int(value) for value in input().split()]
for i in range(3):
    q, v = [int(value) for value in input().split()]
    modelos.append((q, v))

print(backtracking(modelos, qtdeBv, compTd))




