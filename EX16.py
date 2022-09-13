alt = float(input("digite a altura"))
cat1 = float(input("digite o primeiro cateto"))
cat2 = float(input("digite o segundo cateto"))

catsom = (cat1**2 + cat2**2) 
if alt**2==catsom :
    print("é um trinagulo retangulo")
else:
    print("não é um triangulo retangulo")