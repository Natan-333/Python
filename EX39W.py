i = 1

ant = 0
prox = 1
soma = 1

while (i < 31):
    print(prox)
    soma = prox + ant
    ant = prox
    prox = soma
    i = i + 1