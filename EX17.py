sexo = input("Digite seu sexo (M/F)")

alt = float(input('Digite a sua altura em (m): '))
 
peso = float(input('Digite o seu peso (em Kg): '))
 
imc = peso / (alt * alt)

if (sexo == "m") :    
    if imc < 20:
        print("Abaixo do peso!")
    elif imc < 25:
        print("Peso ideal!")
    else:
        print("Acima do peso!")
else:
    if imc < 19:
        print("Abaixo do peso!")
    elif imc < 24:
        print("Peso ideal!")
    else:
        print("Acima do peso!")