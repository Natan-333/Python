v1 = int(input("Digite o número inicial: "))
v2 = int(input("Digite o número final: "))

for v1 in range (v1, (v2+1), 1):
    if (v1 >= 10):
        if (v1 % 2 == 0):
            print(v1)
print("São os números pares no intervalo informado.")
print("Programa Encerrado")