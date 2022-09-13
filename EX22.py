a=float(input("altura"))
b=float(input("base"))
l=float(input("lado"))
ra=float(input("raio"))

print("digite uma opção")

print("1-triângulo")
print("2-quadrado")
print("3-retângulo")
print("4 círculo")
print("5-fim de processo") 

opção = float(input(" digite a opção desejada"))

if opção == 1:
    r = b * a
    print("a área do triângulo é", r)
elif opção == 2:
    r = l * l 
    print("a área quadrado é", r)
elif opção == 3:
    r = b * a
    print("a área retângulo é", r)
elif opção == 4:
    r = 3.14 * ra*ra 
    print("a área círculo é", r)
elif opção == 5:
    r = 0
    print("operação encerrada", r)
else:
    print("erro opção invalida")
            
print("fim do programa, obrigado pela ajuda")