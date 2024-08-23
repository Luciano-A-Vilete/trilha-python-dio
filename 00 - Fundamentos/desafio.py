# Constantes
LIMITE_SAQUES = 3
LIMITE = 500

# Variáveis globais
saldo = 0
extrato = []
numero_saques = 0

# Funções
def exibir_menu():
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    => """
    return input(menu).lower()

def depositar(valor):
    global saldo, extrato
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

def sacar(valor):
    global saldo, extrato, numero_saques

    if valor <= 0:
        print("Operação falhou! O valor informado é inválido.")
        return
    
    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
        return

    if valor > LIMITE:
        print("Operação falhou! O valor do saque excede o limite.")
        return

    if numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques excedido.")
        return

    saldo -= valor
    extrato.append(f"Saque: R$ {valor:.2f}")
    numero_saques += 1
    print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

def exibir_extrato():
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for movimento in extrato:
            print(movimento)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

# Loop principal
def main():
    while True:
        opcao = exibir_menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            depositar(valor)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            sacar(valor)

        elif opcao == "e":
            exibir_extrato()

        elif opcao == "q":
            print("Saindo do sistema. Obrigado por usar nossos serviços!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

# Execução do programa
if __name__ == "__main__":
    main()
