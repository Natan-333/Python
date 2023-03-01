#Crie um programa para cadastrar clientes (nome, email e idade) e pergunte para cada cliente se ele tem ou não conta bancária. Caso o cliente tenha, permita ele cadastrar os dados da conta bancária (agência, número e saldo). Ao final, exibir todos os clientes e suas respectivas contas bancárias, se houver, Faça esse exercício de 2 formas: 1 utilizando Dicionario, tupla e Set 2 Utilizando Lista Tupla e Set
#dicionario tupla e set
nomes = set()
 
Clientes = []

for i in range(0, 2, 1):
    nome = input('digite seu nome')
# verificando se o nome já foi cadastrado antes  

if nome in nomes:
    print('Este nome já foi cadastrado antes. Por favor, digite outro nome.')
    
else:
    nomes.add(nome)

    email = input('digite seu email')
    idade = int(input('digite sua idade'))

PossuiContaBancaria= input('Você possui conta bancária? (s/n): ').lower()

# se o cliente tem conta bancária, pedir as informações da conta e adicioná-las ao dicionário do cliente

if PossuiContaBancaria =='s':
    agencia = input('Digite a agência: ')
    numerodaconta = input('Digite o número da conta: ')
    saldo = float(input('Digite o saldo: '))
    cliente = {'nome': nome, 'email': email, 'idade': idade, 'agencia': agencia, 'numero_conta': numerodaconta, 'saldo': saldo}
else:
    cliente = {'nome': nome, 'email': email, 'idade': idade}

#com Tupla

Clientes.append(cliente)

for cliente in Clientes:
    print('Nome:', cliente['nome'])
print('Email:', cliente['email'])
print('Idade:', cliente['idade'])
if 'agencia' in cliente:
    print('Agência:', cliente['agencia'])
print('Número da conta:', cliente['numero_conta'])
print('Saldo:', cliente['saldo'])
print()