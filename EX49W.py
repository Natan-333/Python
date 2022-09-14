a = int(input("Digite o início do intervalo: "))
b = int(input("Digite o final do intervalo: "))

while (b <= a):
    print("O valor final deve ser maior do que o valor inicial.")
    b = int(input("Digite o final do intervalo: "))

soma = 0

while (a <= b):
    soma = soma + x
    a = x + 1

print(f"A soma dos valores do intervalo é: {soma}")