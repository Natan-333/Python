alt = float(input('Digite a sua altura em (m): '))
 
peso = float(input('Digite o seu peso (em Kg): '))
 
imc = peso / (alt * alt)
 
if imc < 18.5:
    print("Abaixo do peso!")
elif imc >=18.6>=25 :
    print("Peso ideal!")
else: imc >25.1
print("Acima do peso!")