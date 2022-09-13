a = int(input("lado do triângulo"))

b = int(input("lado do triângulo"))

c = int(input("base do triângulo"))

soma = a + b
if (soma>=c):
    print("é um triagulo")
    if soma==(2*c):
        print('este triângulo é equilátero')
    elif a==b and a!=c:
        print('este triângulo é escaleno')
    else:
        print('este triângulo é isóceles')
else:
    print("não é um triangulo")