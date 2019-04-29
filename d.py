# Problema D - Brasileirinho
pe, pv = [int(value) for value in input().split()]
qr = int(input())
pat = int(input())

vitorias, empates = pat // pv, pat % pv
empates, derrotas = empates // pe, empates % pe
derrotas = qr - (vitorias + empates)

print("{} vitoria(s)\n{} empate(s)\n{} derrota(s)".format(vitorias, empates, derrotas))
