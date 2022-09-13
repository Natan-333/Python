a = float(input("valor da aceleração"))
v0 = float(input("valor da velocidade inicial"))
t = float(input("tempo de percurso"))

vf = (v0 + a) * t * 3.6

if (vf <= 40):
    print("velocidade final muito lenta")
elif (40 < vf <= 60):
    print("velocidade permitida")
elif (60 < vf <= 80):
    print("velocidade de cruzeiro")
elif (80 < vf <= 120):
    print("veiculo rápido")
else:
    print("veiculo muito rápido")