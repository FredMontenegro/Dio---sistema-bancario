banco = "AQP - AGIOTAGEM QUEBRA-PERNA"

menu = '''
    Seja bem-vindo ao AQP
    
    Escolha uma das opções:
[1] - Depositar
[2] - Sacar
[3] - Extrato
[9] - Sair
'''

saldo = 0
limite_saque = 3
numero_saques = 3
valor_saque = valor_deposito = 0
historico_depositos = []
historico_saques = []
historico_saldos = [saldo]

while True:

    opcao = str(input(menu)).upper()
    
     
    if opcao == "1":
          
        valor_deposito = float(input("Valor do depósito: R$ "))
        if valor_deposito > 0:
            saldo += valor_deposito
            print("Depósito realizado com sucesso!")
            print(f"Depósito de R$ {valor_deposito:.2f} realizado")

            historico_depositos.append(valor_deposito)

        else:
            print("\nOperação não realizada. Valor inválido")
        print("\n Retornando ao menu...")

    elif opcao == "2":

        valor_saque = float(input("Informe o valor do saque: R$ "))

        if numero_saques <= 3:
            if valor_saque <= limite_saque:
                if valor_saque <= saldo:
                    numero_saques -= 1
                    saldo -= valor_saque
                    print("Saque realizado com sucesso!")
                    print(f"Saque de R$ {valor_saque:.2f} realizado")

                    historico_saques.append(valor_saque)
                
                else:
                    print("Operação não realizada, saldo indisponível!")

            else:
                print("Operação não realizada, limite de saque excedido.")
        
        else:
            print("Operação não realizada, limite de saques diário excedido.")
        
        print("\n Retornando ao menu...")

    elif opcao == "3":

        if len(historico_depositos) == 0 and len(historico_saques) == 0:
            print("Nenhuma operação realizada!")
        else:
            print(f"Saldo inicial: R$ {historico_saldos[0]:.2f}\n")
        if len(historico_depositos) > 0:
            print("depósitos".upper())
            for deposito in historico_depositos:
                print(f"R$ {deposito:.2f}")
        
        if len(historico_saques) > 0:
            print("saques".upper())
            for saque in historico_saques:
                print(f"R$ {saque:.2f}")
            print()
        
        print(f"Saldo atual da conta: R$ {saldo:.2f}")
        print(f"Saques diários restantes: {limite_saque}\n")

    elif opcao == "9":
        print("Obrigado pela preferência! Operação encerrada")

        break
    
    else:
        print("Operação inválida!")




