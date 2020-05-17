#CHECK_POINT-PYTHON
import getpass
import time
from functions import VerificarCPF
from functions import VerificarRG
from functions import VerificarCEP
from functions import VerificarSenhas
from functions import VerificarTilEleitor
from functions import AdicionarTAG
from functions import BuscarTAG
from functions import ExibirTAG


print ("\033[1;35m------------------------------------------------------------------------------------------------------------ ")
print ('''  __        ________   ______   __    __         ______   ________   ______   _______    ______   __    __ 
/  |      /        | /      \ /  |  /  |       /      \ /        | /      \ /       \  /      \ /  |  /  |
$$ |      $$$$$$$$/ /$$$$$$  |$$ | /$$/       /$$$$$$  |$$$$$$$$/ /$$$$$$  |$$$$$$$  |/$$$$$$  |$$ |  $$ |
$$ |      $$ |__    $$ |__$$ |$$ |/$$/        $$ \__$$/ $$ |__    $$ |__$$ |$$ |__$$ |$$ |  $$/ $$ |__$$ |
$$ |      $$    |   $$    $$ |$$  $$<         $$      \ $$    |   $$    $$ |$$    $$< $$ |      $$    $$ |
$$ |      $$$$$/    $$$$$$$$ |$$$$$  \         $$$$$$  |$$$$$/    $$$$$$$$ |$$$$$$$  |$$ |   __ $$$$$$$$ |
$$ |_____ $$ |_____ $$ |  $$ |$$ |$$  \       /  \__$$ |$$ |_____ $$ |  $$ |$$ |  $$ |$$ \__/  |$$ |  $$ |
$$       |$$       |$$ |  $$ |$$ | $$  |      $$    $$/ $$       |$$ |  $$ |$$ |  $$ |$$    $$/ $$ |  $$ |
$$$$$$$$/ $$$$$$$$/ $$/   $$/ $$/   $$/        $$$$$$/  $$$$$$$$/ $$/   $$/ $$/   $$/  $$$$$$/  $$/   $$/ 
                                                                                                           ''' )

print ("------------------------------------------------------------------------------------------------------------\033[m")
print ("O LEAK SEARCH é de forma simplificada uma base de dados com os vazamentos mais atualizados onde o usuário pode pesquisar se suas informações estão circulando onde não deveriam.")
print ("Para utilizar o LEAK SEARCH basta selecionas uma de suas 5 possíveis pesquisas, e digitar com a pontuação correta seu item!")
print ("Além disso foi adicionada uma nova função para trabalhar com TAG's de vazamentos, para utilizá-las, basta selecionar a opção 6 a 8.")

#Base de dados vazados
num_cpf = ["440.550.768-60", "817.223.028-10", "675.241.758-09", "504.175.618-06", "135.311.098-20", "554.632.358-21", "804.360.018-02", "611.588.148-01", "762.959.898-02", "619.230.528-53", "141.894.668-08", "409.891.198-15", "207.606.368-42", "744.689.418-04", "649.945.378-10", "110.099.928-05", "289.826.148-34", "732.287.698-95", "722.785.478-79", "975.913.498-56", "563.308.908-11", "541.743.968-17", "892.899.278-87", "072.095.658-76", "886.523.838-04"]
num_rg = ["36.346.882-1", "14.601.155-7", "32.784.305-6", "11.769.500-2", "50.065.695-2", "47.861.220-5", "23.498.338-3", "46.303.259-7", "48.905.338-5", "36.862.455-9", "49.496.091-7", "28.377.755-2", "50.392.960-8", "36.731.703-5", "16.228.091-9", "23.731.255-4", "17.332.568-3", "22.788.515-6", "43.930.848-3", "50.202.073-8", "49.021.795-3"]
num_cep = ["07851-071", "03702-000", "05521-201", "12446-250", "13340-152", "18705-023", "18076-050", "02022-0350", "04533-011", "09122-055", "13214-867", "04509-903", "12930-970", "13903-442", "13088-012", "12225-852", "15991-422", "13309-340", "07862-080", "16056-873", "07434-313", "13213-080", "08253-420", "03165-000", "01126-030", "16012-527", "12041-016", "06807-000", "14031-480", "13273-275", "07131-340"]
senhas = ["VicsheRsus", "VanVictorious", "@45Plego", "@chenko", "laranjaq31", "asdad2", "abc1212", "alberico_lindos2s2", "me_da_nota_boa", "Zeucursed", "alvocaos9090", "hackserkk1", "time-for-space2232", "enzo-eidy", "deeperinside212", "feccer", "kkjdASDSff2"]
num_title_eleitor = ["377104770191", "513862270175", "408167480132", "417048650132", "226454500191", "842243620132", "645723720108", "335343760175", "205457750140", "136818150132", "078625000191", "147520150108", "644758520108", "080640430159", "281276770132", "154523800116", "234223660191", "285438270116", "750586100191"]
vazamento_conta = {"ALBERICO":["alberico@uol.com.br", "S3nh@", 998], "LUIZ":["luizon@gmail.com", "ULTR4S3NH@", 58]}
opcao = int


while opcao != 9:
    print('''             [1] Pesquisar CPF
             [2] Pesquisar RG
             [3] Pesquisar CEP
             [4] Pesquisar Senha
             [5] Pesquisar Título de Eleitor
             [6] Adicionar uma TAG
             [7] Buscar uma TAG
             [8] Exibir todas as TAG's
             [9] Finalizar o programa''')
    opcao = int(input("Selecione a opção desejada: "))
    
        ###### Verificador de CPF #############
    if opcao == 1:
        VerificarCPF(num_cpf)
        
        ####### Verificador de RG ##############            
    elif opcao == 2:
        VerificarRG(num_rg)

        ###### Verificador de CEP ###############
    elif opcao == 3:
        VerificarCEP(num_cep)

        ###### Verificador de senhas ##############
    elif opcao == 4:
        VerificarSenhas(senhas)

        ###### Verificador de titulo de eleitor ########
    elif opcao == 5:
        VerificarTilEleitor(num_title_eleitor)
    
        ###### Opção para adicionar uma TAG ##############
    elif opcao == 6:
        AdicionarTAG(vazamento_conta)

        ###### Opção para buscar uma TAG ##################
    elif opcao == 7:
        BuscarTAG(vazamento_conta)    
    
        ###### Opção para exibir todas as TAG's ########
    elif opcao == 8:
        ExibirTAG(vazamento_conta)
                
        ###### Opção para finalizar o programa ##########
    
    elif opcao == 9:
        print ("Obrigado por utilizar o \033[;1m\033[1;35mLEAK SEARCH!\033[m")
        time.sleep(2)
        exit()
    
        ###### Caso a opção não esteja dentre as possíveis ########

    elif opcao != 9:
        print("A opção selecionada é inválida, tente novamente!")
        time.sleep(2)

else:
    print("Obrigado por usar o LEAK SEARCH!")
