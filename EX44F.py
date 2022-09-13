a = 10
soma = 0
b = 0

for i in range (0, a, 1):
  n = int(input("Digite um número: "))

  if (i == 0):
    b = n
  elif (n > b):
    b = n

  soma = soma + n

media = soma / a

print("média", media)
print("soma", soma)
print("maior", b)