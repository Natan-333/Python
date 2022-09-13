a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))
c = float(input('Digite o terceiro número: '))

if (a > b and a > c):
    print("O primeiro valor informado é o maior")

if (b > a and b > c):
    print("O segundo valor informado é o maior")

if (c > a and c > b):
    print("O terceiro valor informado é o maior")

if (a == b and a == c):
    print("Os valores são iguais")