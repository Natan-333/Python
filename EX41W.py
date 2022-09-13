quantidade = int(input("Qual é o valor da sequencia? "))
while (quantidade <= 0 or quantidade > 100): 
  quantidade = int(input("O valor da sequência deve ser positivo e menor que cem. Informe novamente: "))

i = 2
seq = 2
soma = 0

while (i < quantidade + 2):
  print(seq)
  soma = soma + seq
  seq = i**2+1
  i = i + 1

print(f"A soma dos valores deu: {soma}")