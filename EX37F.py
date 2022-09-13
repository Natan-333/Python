v = 1

for i in range(1, 20, 1):
    for i in range(1, 21, 1):
        result = v * i 
        print(f"{v} X {i} = {result}")
        i = i + 1

        
        if (i == 21):
            confirme = input("Digite 'OK' para continuar: ")
            
            if (confirme == 'OK'):
                v = v + 1
            else:
                confirme = input("Digite 'OK' para continuar: ")

print("Thank you")