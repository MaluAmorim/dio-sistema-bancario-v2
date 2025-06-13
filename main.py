import time

# Funções de operações bancárias
def saque(*, saldo, valor_saque, limite_valor, extrato, numero_saque, limite_saque):

    if numero_saque >= limite_saque: # Caso a quantidade de saques seja maior ou iqual ao limite de saques o mesmo será impedido
        print("Limite de saques diários atingido.\n")

    # Da continuidade ao saque
    else:
        try:
            if valor_saque > limite_valor: # Caso o valor enserido seja maior do que o limite é informado e solcitado que insira novamente
                print(f"O valor máximo para saque é R${limite_valor:.2f}.\n")

            elif valor_saque > saldo: # Se o valor para saque for maior do que o valor em conta o usuário terá que digitar novamente
                print(f"Saldo insuficiente! Seu saldo atual é de R${saldo:.2f}\n")

            elif valor_saque <= 0: # Informa que o valor tem q ser positivo fazendo o usuário digitar novamente
                print("O valor deve ser positivo.\n")

            else: # Código continua normalmente
                saldo -= valor_saque
                extrato.append(f"Saque: -R${valor_saque:.2f}")
                numero_saque += 1
                print("Saque realizado!\n")
                return saldo, extrato, numero_saque
        
        except ValueError: # Trata erro ao ser inserido um valor string
                print("Entrada inválida. Por favor, digite um número válido. Não utilize vigulas mas sim ponto. Ex.: 275.49\n")


def deposito(saldo, valor_depositado, extrato, /):

    try:
        if valor_depositado > 0: # Caso seja um número positivo da continuidade ao código
            saldo += valor_depositado
            extrato.append(f"Depósito: +R${valor_depositado:.2f}")
            print("Depósito realizado! \n")

        else: # Caso o valor informado seja invalido é informado ao usuário e solicitado novamente a inserção
            print("O valor deve ser positivo.\n")
        return saldo, extrato
    
    except ValueError: # Trata erro ao ser inserido um valor string
        print("Entrada inválida. Por favor, digite um número válido. Não utilize vigulas mas sim ponto. Ex.: 275.49\n")

# Função responsavel por exibir o extrato da conta do usuário
def extrato(saldo, /, *, extrato):

    print("\n--- Extrato ---")
    if not extrato:
        print("Nenhuma movimentação.")
    else:
        for item in extrato:
            print(item)
    print(f"Saldo atual: R${saldo:.2f}")
    print("----------------\n")


# Gerenciamento de dados
usuarios = []
contas = []

# Função responsavel por tratar toda a criação dos usuários
def criar_usuario(nome, data_nascimento, cpf, endereco):
    # Remove qualquer caracter que não seja letra ou número
    cpf = ''.join(filter(str.isdigit, cpf))
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print(f"Erro: CPF {cpf} já cadastrado!\n")
            return
        
    # Dicionário responsavel pelas informações do usuário
    novo_usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }

    usuarios.append(novo_usuario)
    print("Usuário criado com sucesso!\n")

# Função responsavel por tratar toda a criação das contas dos usuários
def criar_conta(cpf):
    usuario = next((user for user in usuarios if user["cpf"] == cpf), None)
    if not usuario:
        print("Usuário não encontrado. Crie um usuário antes de criar uma conta.\n")
        return

    numero_conta = len(contas) + 1
    # Dicionário responsavel pelas informações da conta
    nova_conta = {
        "agencia": "0001",
        "numero_conta": numero_conta,
        "usuario": usuario
    }

    contas.append(nova_conta)
    print(f"Conta criada com sucesso! Agência: 0001 | Conta: {numero_conta}\n")


# Função responsavel por guiar o usuário pelas funções do sistema
def menu():

    # declarando variaveis e seus valores
    saldo = 0.0
    extrato_lista = []
    numero_saque = 0
    LIMITE_SAQUE = 3
    LIMITE_VALOR_SAQUE = 500.0

    # Loop que mantem o sistema funcionando até que seja escolhida a opção 0 para sair
    while True:
        print("""
        ========= MENU =========
        [1] Depositar
        [2] Sacar
        [3] Extrato
        [4] Criar usuário
        [5] Criar conta
        [6] Listar contas
        [0] Sair
        ========================
        """)
        try:
            opcao = int(input("Digite a opção desejada: ").strip())

            # Ao ser escolhida a opção 1 é retorna a função deposito
            if opcao == 1:
                valor = float(input("Informe o valor do depósito: "))
                saldo, extrato_lista = deposito(saldo, valor, extrato_lista)

            # Ao ser escolhida a opção 2 é retorna a função saque
            elif opcao == 2:
                valor = float(input("Informe o valor do saque: "))
                saldo, extrato_lista, numero_saque = saque(
                    saldo=saldo,
                    valor_saque=valor,
                    extrato=extrato_lista,
                    limite_valor=LIMITE_VALOR_SAQUE,
                    numero_saque=numero_saque,
                    limite_saque=LIMITE_SAQUE
                )

            # Ao ser escolhida a opção 3 é retornada a função extrato
            elif opcao == 3:
                extrato(saldo, extrato=extrato_lista)

            # Ao ser escolhida a opção 4 é retornada a função criar usuário
            elif opcao == 4:
                nome = input("Nome completo: ")
                data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
                cpf = input("CPF (somente números): ")
                logradouro = input("Logradouro: ")
                numero = input("Número: ")
                bairro = input("Bairro: ")
                cidade = input("Cidade: ")
                estado = input("Estado (sigla): ")

                endereco = f"{logradouro}, {numero} - {bairro} - {cidade}/{estado}"
                criar_usuario(nome, data_nascimento, cpf, endereco)

            # Ao ser escolhida a opção 5 é retornada a função criar conta
            elif opcao == 5:
                cpf = input("Informe o CPF do usuário: ")
                criar_conta(cpf)

            # Ao ser escolhida a opção 6 é retornada a lista das contas
            elif opcao == 6:
                if not contas:
                    print("Nenhuma conta cadastrada.\n")
                else:
                    for conta in contas:
                        print(f"Agência: {conta['agencia']} | Conta: {conta['numero_conta']} | Titular: {conta['usuario']['nome']}")
                print()

            elif opcao == 0: # Encerra o programa
                print("Agradecemos a preferência, até breve!")
                break

            else: # Trata erro ao ser inserido algum numero que não seja os especificados
                print("Opção inválida. Tente novamente.\n")

        except ValueError: # Trata erro ao ser inserido um valor string
            print("Entrada inválida. Digite somente números.\n")


if __name__ == "__main__":
    print("Abrindo o LumosBank...", end="\r")
    time.sleep(3)
    print("Bem-vindo ao LumosBank!\n")
    menu()