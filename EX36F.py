n1 = 1
n2 = 1
n3 = 1
soma = 3

for n in range(0,21):
    print(n1)
    soma = n1 + n2 + n3
    n1 = n2
    n3 = soma
x = int(input('digite o valor de X: '))

while(x <= 0):
    x = int(input('digite o valor de X:'))

intervalo = int(input('digite o intervalo: '))

while(x > intervalo):
    intervalo = int(input('o intervalo deve ser maior que o valor informado: '))

    i = intervalo

while(i > 0):
    r = x * i
    print('sua tabuada é: ', r)
    i = i -1