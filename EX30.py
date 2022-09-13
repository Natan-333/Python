v=input(float("qual é o valor"))

f=input("Qual é a forma de pagamento? À Vista em Dinheiro ou CHeque (VD ou CH)? À Vista no Cartão de Crédito (VCC)? Em Duas Vezes (DV)? Ou em Quatro Vezes (QV)?")

v1=v -( 0.1 * v)

v2=v -( 0.15 * v)

v3=v + (0.1 * v)

if f == "VD" or f == "CH":
    print("O pagamento é à vista em dinheiro ou cheque e o preço final é igual a " +v1)
elif f == "VCC":
    print("O pagamento final é à vista no cartão de crédito e o preço final é igual a " +v2)
elif f == "DV":
    print ("o pagamento final é em duas vezes sem juros e o preço final é igual a " +v3)
elif f == "QV":
    print ("o pagamento final é em quatro vezes com juros de e o preço dinal é igual a" +v3+v1)

