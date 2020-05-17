import time
import getpass

def VerificarCPF(num_cpf):
    num_cpf_vazamento = (input("Digite o item a ser pesquisado na lista de vazamentos: "))
    for x in num_cpf:
        if x == num_cpf_vazamento:
            print("\033[1;31mO número de cpf {} foi vazado!\033[m".format(num_cpf_vazamento))
            break
    else:
        print("\033[1;32mO número de cpf {} está seguro!\033[m".format(num_cpf_vazamento))
    time.sleep(2)
    resposta = (input('''Deseja realizar uma nova pesquisa?
    [1] Sim!
    [2] Não!
    '''))
    if resposta == "1":
        print("Realizando sua nova pesquisa...")
        time.sleep(2)                    
    else:
        print("Obrigado por utilizar o \033[;1m\033[1;35mLEAK SEARCH!\033[m")
        time.sleep(2)
        exit()
    
    ####### Verificador de RG ##############            

def VerificarRG(num_rg):    
    num_rg_vazamento = (input("Digite o RG que deve ser analisado: "))
    for y in num_rg:
        if y == num_rg_vazamento:
            print("\033[1;31mO número de RG {} foi vazado!\033[m".format(num_rg_vazamento))
            break
    else:
        print("\033[1;32mO número de RG {} está seguro!\033[m".format(num_rg_vazamento))
    time.sleep(2)
    resposta = (input('''Deseja realizar uma nova pesquisa?
    [1] Sim!
    [2] Não!
    '''))
    if resposta == "1":
        print("Realizando uma nova pesquisa...")
        time.sleep(2)                    
    else:
        print("Obrigado por utilizar o \033[;1m\033[1;35mLEAK SEARCH!\033[m")
        time.sleep(2)
        exit()
    
    
    ###### Verificador de CEP ###############
def VerificarCEP(num_cep):
    num_cep_vazamento = (input("Digite o CEP que deve ser analisado: "))
    for z in num_cep:
        if z in num_cep_vazamento:
            print("\033[1;31mO número de CEP {} foi vazado!\033[m".format(num_cep_vazamento))
            break
    else:
        print("\033[1;32mO número de CEP {} está seguro!\033[m".format(num_cep_vazamento))
    time.sleep(2)
    resposta = (input('''Deseja realizar uma nova pesquisa?
    [1] Sim!
    [2] Não!
    '''))
    if resposta == "1":
        print("Realizando uma nova pesquisa...")
        time.sleep(2)                    
    else:
        print("Obrigado por utilizar o \033[;1m\033[1;35mLEAK SEARCH!\033[m")
        time.sleep(2)
        exit()
    ###### Verificador de senhas ##############

def VerificarSenhas(senhas):
    senha_vazamento = getpass.getpass("Digite a senha que deve ser analisada: ")
    for a in senhas:
        if a in senha_vazamento:
            print("\033[1;31mEstá senha foi vazada! Troque o mais rápido possível!\033[m")
            break
    else:
        print("\033[1;32mEsta senha está segura!\033[m")
    time.sleep(2)
    resposta = (input('''Deseja realizar uma nova pesquisa?
    [1] Sim!
    [2] Não!
    '''))
    if resposta == "1":
        print("Realizando uma nova pesquisa...")
        time.sleep(2)                    
    else:
        print("Obrigado por utilizar o \033[;1m\033[1;35mLEAK SEARCH!\033[m")
        time.sleep(2)
        exit()
    ###### Verificador de titulo de eleitor ########
def VerificarTilEleitor(num_title_eleitor):
    title_eleitor_vazamento = (input("Digite o título de eleitor que deve ser analisado: "))
    for b in num_title_eleitor:
        if b in title_eleitor_vazamento:
            print("\033[1;31mO número de título de eleitor {} foi vazado!\033[m".format(num_title_eleitor))
            break
    else:
        print("\033[1;32mO número de  título de eleitor {} está seguro!\033[m".format(num_title_eleitor))
    time.sleep(2)
    resposta = (input('''Deseja realizar uma nova pesquisa?
    [1] Sim!
    [2] Não!
    '''))
    if resposta == "1":
        print("Realizando uma nova pesquisa...")
        time.sleep(2)                    
    else:
        print("Obrigado por utilizar o \033[;1m\033[1;35mLEAK SEARCH!\033[m")
        time.sleep(2)
        exit()

########## Opção para adicionar uma TAG ##############
def AdicionarTAG(vazamento_conta):
    pergunta = "S"
    while pergunta =="S":
        TAG = input("Adicione a tag do vazamento: ").upper()
        vazamento_conta[TAG] = [input("Digite o e-mail do vazamento: "), input("Digite a senha: "), int(input("Digite a validade da conta: "))]
        print ("\033[1;32mTAG adicionada com sucesso!\033[m")
        time.sleep(2)
        pergunta = input("Deseja cadastrar mais um email?(S/N) ").upper()
        time.sleep(2)
    
########## Opção para buscar uma TAG ##################
def BuscarTAG(vazamento_conta):
    buscatag = input("Digite a TAG a ser buscada: ").upper()
    if vazamento_conta.get(buscatag) != None:
        lista = vazamento_conta.get(buscatag)
        print("\nEmail......... ", lista[0])
        print("Senha......... ", lista[1])
        print("Validade...... ", lista[2])
        tmp = input("precione enter para continuar")
    else:
        print("\033[1;31mTag nao encontrada!\033[m")
    

    ###### Opção para exibir todas as TAG's ########

def ExibirTAG(vazamento_conta):
    for tag, lista in vazamento_conta.items():
        print("\nTag...........", tag)
        print("Email......... ", lista[0])
        print("Senha......... ", lista[1])
        print("Validade...... ", lista[2])       
    tmp = input("Precione enter para continuar")
