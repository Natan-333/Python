n = int(input("Digite o valor de n: "))
while (n <= 0): n = int(input("Informe somente valores positivos: "));

fatorial = 1
m = 2
while (m <= n):
    fatorial = fatorial*m

    m = m + 1
    
    if (m - 1 == n):
        print(f"O valor de {n}! é = {fatorial}")

        resposta = input("\nDeseja executar o programa novamente? 'SIM' ou 'NAO': ")
        while (resposta != 'SIM' and resposta != 'NAO'): 
            resposta = input("Deseja executar o programa novamente? 'SIM' ou 'NAO': ")
        if (resposta == 'SIM'): 
            m = 2
            fatorial = 1
            
            n = int(input("Digite o valor de n: "))
            while (n <= 0): n = int(input("Informe somente valores positivos: "));