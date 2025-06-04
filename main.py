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
    endereco = {logradouro: logradouro,
                numero_propriedade: numero_propriedade,
                bairro: bairro,
                cidade: cidade,
                sigla_estado: sigla_estado}
    
    # Dicionário responsavel pelas informações do usuário
    usuario = {nome: nome,
               data_nascimento: data_nascimento,
               cpf: cpf,
               endereco: endereco}
    
    nome = input("Informe o nome do usuário: ")
    data_nascimento = input("Informe a data de nascimento deste do usuário: ")
    cpf = input("Informe o CPF do usuário: ")
    endereco = input("Informe o endereço do usuário: ")
     
    # Remove qualquer caracter que não seja letra ou número
    cpf_formatado = ''.join(filter(str.isdigit, cpf))

    for usuario in usuarios:
        if usuario['cpf'] == cpf_formatado:
            print(f"Erro: CPF {cpf_formatado} ja cadastrado!")
            return None

# Função responsavel por tratar toda a criação das contas dos usuários
def criar_conta(agencia, numero_conta, usuario):
    agencia = 0001
    numero_conta = 1
    
# Função responsavel por tratar os saques realizados na conta
def saque(*, saldo, valor_saque, limite_valor, numero_saque, limite_saque):
    limite_valor = 500.0
    limite_saque = 3
    numero_saque = 0
    saques_realizados = []

    if numero_saque >= limite_saque: # Caso a quantidade de saques seja maior ou iqual ao limite de saques o mesmo será impedido
                print("Limite de saques diários atingido.\n")
    
    # Da continuidade ao saque
    else:
        try:
            valor_saque = float(input("Digite o quantia a ser retirada: ")) # Recebe o valor a ser retirado da conta

            if valor_saque > limite_valor: # Caso o valor enserido seja maior do que o limite é informado e solcitado que insira novamente
                print(f"O valor máximo para saque é R${limite_valor:.2f}.\n")

            elif valor_saque > saldo: # Se o valor para saque for maior do que o valor em conta o usuário terá que digitar novamente
                print(f"Saldo insuficiente! Seu saldo atual é de {saldo:.2f}\n")

            elif valor_saque <= 0: # Informa que o valor tem q ser positivo fazendo o usuário digitar novamente
                print("O valor deve ser positivo.\n")

            else: # Código continua normalmente
                saldo -= valor_saque
                numero_saque += 1
                saques_realizados += [valor_saque]
                print("Saque realizado!\n")

                return saldo
                
        except ValueError: # Trata erro ao ser inserido um valor string
                print("Entrada inválida. Por favor, digite um número válido. Não utilize vigulas mas sim ponto. Ex.: 275.49\n")

# Função responsavel por tratar os depósitos realizados na conta
def deposito(saldo, valor_deposito, /):

    try:
        valor_deposito = float(input("Digite a quantia a ser depositada: ")) # Recebe o valor a ser depositado

        if valor_deposito > 0: # Caso seja um número positivo da continuidade ao código
            saldo += valor_deposito
            print("Depósito realizado! \n")
            return saldo

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
            opcao = int(input("Digite a opção desejada: ")) # Recebe a opção escolhida pelo usuário
            # Ao ser escolhida a opção 1 é retoranada a função deposito
            if opcao == 1:
                return deposito
                
            # Ao ser escolhida a opção 2 é retoranada a função saque
            elif opcao == 2:
                return saque
                
            # Ao ser escolhida a opção 3 é retoranada a função extrato
            elif opcao == 3:

                return extrato
            
            # Ao ser escolhida a opção 4 é retoranada a função criar usuário
            elif opcao == 4:
                return criar_usuario
            
            # Ao ser escolhida a opção 5 é retoranada a função criar conta
            elif opcao == 5:
                return criar_conta
            
            elif opcao == 0: # Encerra o programa
                print("Agradecemos a preferência, até breve!")
                break
            
            else: # Trata erro ao ser inserido algum numero que não seja os especificados
                print("Opção inválida. Tente novamente.\n")

        except ValueError: # Trata erro ao ser inserido um valor string
                        print("Entrada inválida. Digite somente números. \n")
