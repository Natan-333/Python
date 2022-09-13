quanti = int(input("Informe a quantidade: "))
while (quanti <= 0 or quanti > 20): 
  quanti = int(input("O valor da sequência deve ser positivo e menor que vinte. Informe novamente: "))

soma = 0
a = 0
b = 0
c = 0
d = 0
r = 'NAO'

i = 0
while (i < quanti):
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
   
  i = i + 1

  if (i == quanti):
    print(f"Maior valor informado: {a}")
    print(f"Menor valor informado: {b}")
    print(f"Soma dos valores informado: {soma}")
    print(f"Média dos valores informados: {media}")
    print(f"Porcentagem dos valores positivos: {(c * 100) / quanti}%")
    print(f"Porcentagem dos valores negativos: {(d * 100) / quanti}%")
    
    resposta = input("\nDeseja executar o programa novamente? 'SIM' ou 'NAO': ")
    while (resposta != 'SIM' and resposta != 'NAO'): 
      resposta = input("Deseja executar o programa novamente? 'SIM' ou 'NAO' ")
    if (resposta == 'SIM'): 
      soma = 0
      a = 0
      b = 0
      c = 0
      d = 0
      quanti = int(input("Informe a quantidade: "))
      while (quanti <= 0 or quanti > 20): 
        quanti = int(input("O valor da sequência deve ser positivo e menor que vinte. Informe novamente: "))
      i = 0