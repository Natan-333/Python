valor = int(input("Informe um valor qualquer: "))

while (valor <= 0): 
    valor = int(input("Informe um valor positivo: "))

i = 1
while (i < 11):
    resultado = valor * i
    print(f"{valor} X {i} = {resultado}")
    i = i + 1	