n = int(input("digite o valor de n: "))

while(n < 0):
    print("erro, o valor deve ser positivo")
    n =("digite o valor de n: ")

while(n > 100):
    print("o valor de n deve ser menor que 100")
    n = int(input("digite o valor de de n: "))

a = 1
b = 1
r = a + b + n

for i in range(1, 100, 1):
    print(r)
    b = a
    a = n
    n = r
    r = n + a + b