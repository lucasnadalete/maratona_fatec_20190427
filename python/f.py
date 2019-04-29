# Problema F - Organização dos Livros
qids = int(input())
ids = input().split()
for i in range(qids):
    for j in range(i + 1, qids):
        if (int(ids[i][-1]) > int(ids[j][-1])):
            ids.insert(i, ids[j])
            del ids[j + 1]
print(' '.join(ids))