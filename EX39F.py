anterior = 0
proxima = 1
soma = 1

for num in range(0,31):
    print(anterior)

    soma = proxima + anterior
    anterior = proxima
    proxima = soma