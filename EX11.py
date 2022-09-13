a = int(input("base do retangulo"))

b = int(input("altura do retangulo"))

area = b * a

print(area)

T = area
if (T > 100):
    print("terreno normal")
else:
    print("terreno grande!")