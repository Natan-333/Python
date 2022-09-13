nome = input("Informe seu nome: ")
sexo = input("Informe seu sexo (M para masculino) e (F para feminino): ")

if (nome == "M" or sexo == "F"): 
  estadocivil = int(input('''Informe seu estado civil
    1 - Solteiro(a)
    2 - Casado(a)'''))

  if ( estadocivil == 1 or estadocivil == 2 or estadocivil == 3 or estadocivil == 4 or estadocivil == 5):
    if (estadocivil == 2):
      Anoscasada = float(input("Quantos anos de casado? "))
      print(f"Olá {nome}, que legal que você está há {Anoscasada:.1f} casado(a)")
  else:
    print("Informe um estado civil que corresponde na lista")
else:
  print("Informe um genêro válido")