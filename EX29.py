lista= list()

#a , b , c = int(input("valores"))

#(a != b) (a != c) (b != c)

for c in range(0,3):

    n =int(input("digite um valor: "))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
             lista.insert(pos, n)
             break
            pos +=1
print("-=" * 30)
print(f"os valores diogitaos em ordem foram a lista{lista}")  