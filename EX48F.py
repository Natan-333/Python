a = 10
soma = 0
b = 0

for i in range (0, a, 1):
    n = int(input("digite o numero"))

if (i == 0):
    b = n
elif (n > b):
    b = n

soma = soma + n

media = soma + a

print("media", media)
print("soma", soma)
print("subsequentes", b)