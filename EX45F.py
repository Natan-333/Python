quanti = int(input("Informe a quantidade: "))
while (quanti <= 0 or quanti > 20): 
  quanti = int(input("O valor da sequência deve ser positivo e menor que vinte. Informe novamente: "))

soma = 0
a = 0
b = 0
c = 0
d = 0

i = 0
for i in range (i, quanti, 1):
  n = int(input("Digite um número: "))

  if (n <= 0):
    d = d + 1
  elif (n > 0):
    c = c + 1

  if (i == 0):
    a = n
    b = n
  elif (n > a):
    a = n
  elif (n < b):
    b = n

  soma = soma + n

media = soma / quanti

print(f"\nMaior valor informado: {a}")
print(f"\nMenor valor informado: {b}")
print(f"\nSoma dos valores informado: {soma}")
print(f"\nMédia dos valores informados: {media}")
print(f"\nPorcentagem dos valores positivos: {(c * 100) / quanti}%")
print(f"\nPorcentagem dos valores negativos: {(d * 100) / quanti}%")