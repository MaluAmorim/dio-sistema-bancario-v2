import time

# Definindo o valor das variáveis e constantes
"""saldo = 0.0
depositos_realizados = 0
valor_dos_depositos = []
saques_realizados = 0
valor_dos_saques = []
LIMITE_SAQUES = 3
LIMITE_VALOR_SAQUE = 500.0
"""
print("Abrindo o LumosBank...", end="\r")
time.sleep(3)

print("Bem vindo ao LumosBank! \n")

opcao = 0

# Função responsavel por tratar toda a criação dos usuários
def criar_usuario(nome, data_nascimento, cpf, endereco):
    # Dicionário responsavel por armazenar as informações de endereço
    
    # Dicionário responsavel pelas informações do usuário
    usuarios = {nome: nome,
               data_nascimento: data_nascimento,
               cpf: cpf,
               endereco: endereco}
     
    # Remove qualquer caracter que não seja letra ou número
    cpf_formatado = ''.join(filter(str.isdigit, cpf))

    for usuario in usuarios:
        if usuario['cpf'] == cpf_formatado:
            print(f"Erro: CPF {cpf_formatado} ja cadastrado!")
            return None

# Função responsavel por tratar toda a criação das contas dos usuários
def criar_conta(agencia, numero_conta, usuario):

    contas = {agencia: agencia,
              numero_conta: numero_conta,
              usuario: usuario}
    

    
# Função responsavel por tratar os saques realizados na conta
def saque(*, saldo, valor_saque, limite_valor, extrato, numero_saque, limite_saque):

    if numero_saque >= limite_saque: # Caso a quantidade de saques seja maior ou iqual ao limite de saques o mesmo será impedido
                print("Limite de saques diários atingido.\n")
    
    # Da continuidade ao saque
    else:
        try:
            if valor_saque > limite_valor: # Caso o valor enserido seja maior do que o limite é informado e solcitado que insira novamente
                print(f"O valor máximo para saque é R${limite_valor:.2f}.\n")

            elif valor_saque > saldo: # Se o valor para saque for maior do que o valor em conta o usuário terá que digitar novamente
                print(f"Saldo insuficiente! Seu saldo atual é de {saldo:.2f}\n")

            elif valor_saque <= 0: # Informa que o valor tem q ser positivo fazendo o usuário digitar novamente
                print("O valor deve ser positivo.\n")

            else: # Código continua normalmente
                saldo -= valor_saque
                numero_saque += 1
                print("Saque realizado!\n")

                return saldo, extrato
                
        except ValueError: # Trata erro ao ser inserido um valor string
                print("Entrada inválida. Por favor, digite um número válido. Não utilize vigulas mas sim ponto. Ex.: 275.49\n")

# Função responsavel por tratar os depósitos realizados na conta
def deposito(saldo, valor_depositado, extrato, /):

    try:
        if valor_depositado > 0: # Caso seja um número positivo da continuidade ao código
            saldo += valor_depositado
            print("Depósito realizado! \n")
            return saldo, extrato

        else: # Caso o valor informado seja invalido é informado ao usuário e solicitado novamente a inserção
            print("O valor deve ser positivo.\n")
            time.sleep(3)

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

# Função responsavel por guiar o usuário pelas funções do sistema
def menu():

    LIMITE_SAQUE = 3
    LIMITE_VALOR_SAQUE = 500.0

    saldo = 0.0
    extrato = []
    numero_saque = 0

    usuarios = []
    contas = []
    numero_conta = 1
    AGENCIA = "0001"

    # Loop que mantem o sistema funcionando até que seja escolhida a opção 4 para sair
    while opcao != 0:
        print("""
            ========= MENU =========
            [1] Depositar
            [2] Sacar
            [3] Extrato
            [4] Criar usuário
            [5] Criar conta
            [0] Sair
            ========================
            """)
        try:
            opcao = int(input("Digite a opção desejada: ")).strip() # Recebe a opção escolhida pelo usuário
            # Ao ser escolhida a opção 1 é retorna a função deposito
            if opcao == 1:
                return deposito
                
            # Ao ser escolhida a opção 2 é retorna a função saque
            elif opcao == 2:

                valor = float(input("Informe o valor do saque: "))

                saldo, extrato, numero_saque = saque(
                saldo=saldo,
                valor_saque=valor,
                extrato=extrato,
                limite_valor=LIMITE_VALOR_SAQUE,
                numero_saque=numero_saque,
                limite_saque=LIMITE_SAQUE
            )
                
            # Ao ser escolhida a opção 3 é retornada a função extrato
            elif opcao == 3:

                return extrato
            
            # Ao ser escolhida a opção 4 é retornada a função criar usuário
            elif opcao == 4:
                
                endereco = {logradouro: logradouro,
                numero_propriedade: numero_propriedade,
                bairro: bairro,
                cidade: cidade,
                sigla_estado: sigla_estado}

                nome = input("Informe o nome do usuário: ")
                data_nascimento = input("Informe a data de nascimento do usuário: ")
                cpf = input("Informe o CPF do usuário: ")

                nome, data_nascimento, cpf = criar_usuario(
                nome=nome,
                data_nascimento=data_nascimento,
                cpf=cpf)
            
            # Ao ser escolhida a opção 5 é retornada a função criar conta
            elif opcao == 5:
                return criar_conta
            
            elif opcao == 0: # Encerra o programa
                print("Agradecemos a preferência, até breve!")
                break
            
            else: # Trata erro ao ser inserido algum numero que não seja os especificados
                print("Opção inválida. Tente novamente.\n")

        except ValueError: # Trata erro ao ser inserido um valor string
                        print("Entrada inválida. Digite somente números. \n")

if __name__ == "__menu__":
    menu()