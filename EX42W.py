seq = int(input("Qual é o valor do termo?"))

while (seq <= 0 or seq > 50):
    seq = int(input("O valor da sequência de termos deve ser positivo e menor que cinquenta. Informe novamente: "))

a = 1
b = 2
i = 1
soma = 0

while (i < seq):
    div = a / b
    soma = soma + div
    print(f"{i}. {a}/{b}")
    a = a + 1
    b = b + 1
    i = i + 1

print("A soma deu: %.2f" % soma)