a=float(input("valor a"))
b=float(input("valor b"))

print("digite uma opção")

print("1-multiplicação")
print("2-adição")
print("3-divisão")
print("4-subtração")
print("5-fim de processo") 

opção = float(input(" digite a opção desejada"))

if opção == 1:
    r = a * b
    print("a multiplicação é", r)
elif opção == 2:
    r = a + b  
    print("a soma é", r)
elif opção == 3:
    r = a / b
    print("a divisão é", r)
elif opção == 4:
    r = a - b
    print("a subtração é", r)
elif opção == 5:
    r = a / b
    print("operação encerrada", r)
else:
    print("erro opção invalida")
            
print("fim do programa, obrigado pela ajuda")