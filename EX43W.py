seq = int(input("Qual é o valor do termo?"))

while (seq <= 0) or (seq > 50):
    seq = int(input("O valor da sequência de termos deve ser positivo e menor que cinquenta. Informe novamente: "))

a = 1
b = 2
i = 1
soma = 0

while (i < seq):
    a = (i ** 2) + 1
    b = (i ** 3)
    divisao = a / b
    if (i == 1): print(f'{a}')
    else: print(f"{a}/{b}")
    i = i + 1
    soma = soma + divisao

print('A soma é: %.2f' %soma)