valor = 1

while (valor < 20):
    for i in range(1, 21, 1):
        resultado = valor * i 
        print(f"{valor} X {i} = {resultado}")
        i = i + 1

        
        if (i == 21):
            avalie = input("Digite 'OK' para continuar: ")
            
            if (avalie == 'OK'):
                valor = valor + 1
            else:
                avalie = input("Digite 'OK' para continuar: ")

print("Thank you")