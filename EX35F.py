v = int(input("Informe um valor qualquer: "))

while (v <= 0): 
    v = int(input("Informe um valor positivo: "))

for i in range(1, 11, 1):
    r = v * i 
    print(f"{v} X {i} = {r}")
    i = i + 1