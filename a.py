# Problema A - Alarme
entrada = input().split()
indexN1 = 0
n1 = int(entrada[indexN1])
indexN2 = n1 + 1
n2 = int(entrada[indexN2])

setN1 = []
setN2 = []
indexN1 += 1
indexN2 += 1
while indexN1 <= n1 or indexN2 <= (n1 + n2 + 1):
    if indexN1 <= n1:
        setN1.append(entrada[indexN1].strip())
        indexN1 += 1
    if indexN2 <= (n1 + n2 + 1):
        setN2.append(entrada[indexN2].strip())
        indexN2 += 1

result = list(set(setN1) & set(setN2))

output = 'OK' \
    if len(result) == 0 \
    else ' '.join(result) + (' OK' \
                             if len(result) < 3  \
                             else ' PERIGO')

print(output)