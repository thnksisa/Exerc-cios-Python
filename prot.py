# 1° caso: Se a pessoa gostaria de realizar um cadastro, pois ela ainda não tem uma conta.
import os
# Cores:
vermelho = '\033[91m'
negrito = '\033[1m'
amarelo = '\033[93m'
verde = '\033[92m'
fim = '\033[0m'


# 1° bloco:
def informacoesparacadastro():
    print("-"*150)
    print(f'''
    Opa, verificamos em nossos dados e você não possui cadastro em nosso banco de doações.
        
    Vamos iniciar o seu cadastro para que você possa contribuir com a doação de sangue e salvar vidas!  🩸
    ''')
    print("-"*150)

    print(f"\n\nImportante!")
    print("\nAntes de realizarmos o seu cadastro,\nverifique se você atende às condições de um doador de sangue ideal:\n")
    print("-"*150)
    print(f'''{negrito}{verde}Quem pode doar sangue? ✅\n{fim}
    - Ter entre 16 e 69 anos.\n
    Sendo que a primeira doação deve ter sido feita antes dos 60 anos.
    Pessoas menores de idade poderão doar somente mediante apresentação de
    autorização formal assinada por um dos pais ou responsável legal\n
    - Peso mínimo igual ou acima de 50kg.\n
    - Boa alimentação e condições de saúde.\n
    - Estar bem alimentado, com refeições leves e uma boa noite de sono antes da doação.
    ''')

    print(f'''{negrito}{amarelo}Quem não pode doar sangue por fatores temporários? ⚠️\n{fim}
    - Se esteve gripado, com febre ou infecção recente.
    - Se está grávida ou amamentando.
    - Pessoas que tiveram relações sexuais ocasionais nos últimos 12 meses, independente do uso de preservativos.
    - Tatuagem, micropigmentação, maquiagem definitiva, brincos e piercings – 06 meses a 1 ano (Será avaliado condições de segurança do procedimento).
    - Se a pessoa haver doenças hematológicas ou câncer.
    ''')

    print(f'''{negrito}{vermelho}Quem não pode doar? ❌{fim}
    - Hepatite após os 11 anos.
    - HIV/AIDS.
    - Doença de Chagas.
    - Câncer ou doenças hematológicas graves.
    - Uso de drogas injetáveis ilícitas.\n''')
    print("-"*150)

# Verifica se o usuário quer continuar no programa:
# 2° bloco:
def continuarprog():
    while True:
        pergunta = input("Você está nas condições para um doador de sangue ideal e deseja continuar no programa? (Sim/Não)\n>").lower()
        if pergunta == "sim":
            print("-"*150)
            print("Que bom! Ficamos felizes pela sua iniciativa. Vamos iniciar o cadastro:")
            print("-"* 150)
            return True
        elif pergunta == "nao" or pergunta == "não":
            print("Ok, vamos finalizar o programa! Obrigada por se interessar em doar sangue.")
            print("-"*150)
            break
        else:
            print("Resposta inválida, por favor insira sim ou não.")
            print("-"*150)
            continue
        


def nome_cadastro():
    while True:
        nome = input("Qual o seu nome completo?\n> ").title().strip()
        if all(pedaco.isalpha() for pedaco in nome.split()):
            return nome
        else:
            print("Por favor, insira um nome válido.")
            continue


def cpf_cadastro():
    while True:
        cpf = input("Insira seu cpf, sem traços ou caracteres especiais:\n> ").strip()
        if cpf.isdigit() == False:
            print("Por favor, insira um cpf válido.")
            continue
        else:
            cpf = int(cpf)
            return cpf

def genero_cadastro():
    while True:
        genero = input("Insira seu gênero, por favor (Feminino/Masculino):\n> ").strip().lower()
        if genero in ["feminino", "masculino", "f", "m"]:
            return genero
        else:
            print("Por favor, insira masculino ou feminino.")
            continue

def telefone_cadastro():
    while True:
        try:
            telefone1 = int(input("Insira seu telefone para contato:\n> "))
            print(f"O telefone digitado foi '{telefone1}'")
            return telefone1
        
        except ValueError:
            print("Por favor, insira um valor correto para o número de telefone.")
            
def email_cadastro():
    while True:
        try:
            email = input("Digite um e-mail para notificarmos você!\n> ")
            if "@gmail" in email:
                return email
        except ValueError:
            print("Por favor, insira um valor correto para o e-mail.")
    
def tipo_sanguineo_cadastro():
    while True:
        try:
            tipo_sanguineo_cadastro = input("Insira o seu tipo sanguíneo: (A+, B+, O+, AB+, AB-, O-, A-, B-)\n>").strip().upper()
            if tipo_sanguineo_cadastro in ["A-", "B-", "AB-", "O-", "AB+", "A+", "B+", "O+"]:
                return tipo_sanguineo_cadastro
        except:
            print("Insira um tipo sanguíneo válido.")

def parceiro_fixo_cadastro():
    while True:
        parceiro_fixo = input("Você tem um parceiro fixo? (S/N)\n>").strip().lower()
        
        if parceiro_fixo in ["sim", "s"]:
            try:
                duracao = int(input("Aproximadamente, há quantos meses estão juntos?\n> "))
            
                if duracao <= 5:
                    print("Opa! Infelizmente não podemos continuar seu cadastro. Você só pode doar sangue se tem um parceiro fixo há mais de seis meses.")
                    return None
                else:
                    return parceiro_fixo 
            except ValueError:
                print("Digite o tempo em meses os quais estão juntos, aproximadamente. Valores numéricos são aceitos.")
        

        elif parceiro_fixo in ["nao", "não", "n"]:
            preservativo = input("Você usou preservativo em todas as suas relações, nos últimos 12 meses? (S/N)\n>").strip().lower()
            
            if preservativo in ["sim", "s"]:
                return parceiro_fixo  
            elif preservativo in ["nao", "não", "n"]:
                print("Opa! Infelizmente não podemos continuar seu cadastro pois relações sexuais sem o uso de preservativo prejudica a doação sanguínea.")
                return None
            else:
                print("Digite uma resposta válida: 'sim' ou 'não'.")
        
        else:
            print("Por favor, insira uma resposta válida: 'sim' ou 'não'.")

def tratamento_cadastro():
    while True:
        tratamento = input("Você fez tratamento hematológico e/ou passou por um tratamento de câncer? (S/N)\n>").strip().lower()
        if tratamento in ["sim","s"]:
            print("Opa! Não podemos finalizar seu cadastro. Pessoas que realizaram tratamentos hematológicos ou contra o câncer recentemente não podem doar sangue.")
            return None
        elif tratamento in ["nao", "não", "n"]:
            return tratamento
        else:
            print("Por favor, digite respostas de sim e não.")
            continue

def tatuagem_piercing_cadastro():
    while True:
        tatuagem_piercing = input("Você fez alguma tatuagem ou colocou piercing recentemente? (S/N)\n>").strip().lower()
        if tatuagem_piercing in ["sim", "s"]:
            try:
                # Pergunta quanto tempo passou desde o último procedimento
                tempo = int(input("Quantos meses se passaram desde sua última tatuagem ou piercing?\n> "))
                if tempo < 6:
                    print("Opa! Infelizmente não podemos continuar seu cadastro. Você precisa esperar 6 meses após o procedimento para doar sangue.")
                    return None
                else:
                    return tatuagem_piercing 
            except ValueError:
                print("Por favor, insira um valor numérico válido para o tempo em meses.")
        
        elif tatuagem_piercing in ["nao", "não", "n"]:
            return tatuagem_piercing
        
        else:
            print("Resposta inválida. Por favor, insira 'sim' ou 'não'.")

# 4° bloco:
# Colocando as informações no dicionário:
pessoa = {}

# função para cadastro cancelado:
def cadastro_cancelado():
    print("Cadastro cancelado.\nObrigada por se interessar em doar sangue.")

informacoesparacadastro()
if continuarprog() is True:
    while True:
        pessoa["nome"] = nome_cadastro()
        pessoa["cpf"] = cpf_cadastro()
        pessoa["gênero"] = genero_cadastro()
        pessoa["email"] = email_cadastro()
        pessoa["telefone"] = telefone_cadastro()
        pessoa["tipo sanguíneo"] = tipo_sanguineo_cadastro()

        parceiro_fixo = parceiro_fixo_cadastro()
        if parceiro_fixo is None:
            cadastro_cancelado()
            break
        else:
            pessoa["parceiro_fixo"] = parceiro_fixo
        
        tratamento = tratamento_cadastro()
        if tratamento is None:
            cadastro_cancelado()
            break
        else:
            pessoa["tratamento"] = tratamento
        
        tatuagem_piercing = tatuagem_piercing_cadastro()
        if tatuagem_piercing is None:
            cadastro_cancelado()
            break
        else:
            pessoa["tatuagem e piercing"] = tatuagem_piercing

# Salvando os dados em um arquivo .txt:
