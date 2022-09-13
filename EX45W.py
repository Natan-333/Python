quanti = int(input("Informe a quantidade: "))
while (quanti <= 0 or quanti > 20): 
  quanti = int(input("O valor da sequência deve ser positivo e menor que vinte. Informe novamente: "))

soma = 0
a = 0
b = 0
c = 0
d = 0

i = 0
while (i < quanti):
  number = int(input("Digite um número: "))

  if (number <= 0):
    d = d + 1
  elif (number > 0):
    c = c + 1

  if (i == 0):
    a = number
    b = number
  elif (number > a):
    a = number
  elif (number < b):
    b = number

  soma = soma + number
  i = i + 1

avarage = soma / quanti

print(f"Maior valor informado: {a}")
print(f"Menor valor informado: {b}")
print(f"Soma dos valores informado: {soma}")
print(f"Média dos valores informados: {avarage}")
print(f"Porcentagem dos valores positivos: {(c * 100) / quanti}%")
print(f"Porcentagem dos valores negativos: {(c * 100) / quanti}%")