valor = int(input("Informe um valor qualquer: "))

while (valor <= 0): 
    valor = int(input("Informe um valor positivo: "))

ini = int(input("Informe o ínicio do intervalo: "))
fim = int(input("Informe o final do intervalo: "))

while (fim <= ini): 
    fim = int(input("O valor final do intervalo deve ser maior que o valor inicial: "))

i = ini
while (i <= fim):
    resultado = valor * i
    print(f"{valor} X {i} = {resultado}")
    i = i + 1