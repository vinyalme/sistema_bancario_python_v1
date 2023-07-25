#as letras foram colocadas em maiúsculas para facilitar na execução do sistema
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d": #operação de Deposito 
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:  #evita ter depósitos negativos
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:  #mensagem é exibida, caso tente depositar valores negativos
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":  #operação de Saque
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo: #mensagem é exibida, caso tenha excedido o saldo
            print(f"Operação falhou! Você não tem saldo suficiente. Salto atual R$ {saldo:.2f}")

        elif excedeu_limite: #mensagem é exibida, caso tenha excedido o limite
            print("Operação falhou! O valor do saque excede o limite. Limite é de R$ 500")

        elif excedeu_saques: #mensagem é exibida, caso tente tenha excedido o saque
            print("Operação falhou! Número máximo de 3 (três) saques excedidos.")

        elif valor > 0:  #evita ter saques valores negativos
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:  #mensagem é exibida, caso tente sacar valores negativos
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":  #operação de Extrato
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":  #operação de Sair da conta
        break

    else:  #mensagem é exibida, caso tenha colocado uma letra invalida
        print("Operação inválida, por favor selecione novamente a operação desejada.")