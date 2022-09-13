a = 10
soma = 0
b = 0

i = 0
while (i < a):
  n = int(input("Digite um número: "))

  if (i == 0):
    b = n
  elif (n > b):
    b = n

  soma = soma + n
  i = i + 1

media = soma / a

print("média", media)
print("soma", soma)
print("maior", b)