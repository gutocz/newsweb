# Record texts

# Imports
import Screens.Menu.Menus_screen as Mm
import Services.Users_services as Us
import Screens.Login.Login_screen as Ls
import Util.Util_functions as Uu
directoryUsers = './Users'

# Texts for records of users
def register_txt():
    print('╔══════════════════╗')
    print('║ Menu de Cadastro ║')
    print('╚══════════════════╝')

    
def adm_or_pub_txt():
    print('╔═══════════════════════════╗')
    print('║ Como deseja se registrar? ║')
    print('║       1 - Jornalista      ║')
    print('║       2 - Leitor          ║')
    print('║       3 - Voltar          ║')
    print('╚═══════════════════════════╝')
    
    options = input('Selecione uma das opções acima: ')
    match options:
       
        case '1':
            register_adm_txt()
       
        case '2':
            register_pub_txt()
      
        case '3':
            Mm.menu_txt()
     
        case _:
            print('Opção inválida.')
            adm_or_pub_txt()



def register_adm_txt():
    print('╔═════════════════════╗')
    print('║ Cadastro Jornalista ║')
    print('╚═════════════════════╝')
    
    reg_name = input('Nome completo: ')
    
    reg_username = input('Nome de usuário: ')
    '''
    if reg_username == Uu.exists_dir(directoryUsers + '/' + reg_username):
        print('Nome de usuário já está em uso')
        reg_username = input('Tente outro nome de usuário: ')
    '''
    reg_pass = input('Digite sua senha: ')
    
    while len(reg_pass) < 6:
        reg_pass = input('Digite uma senha com 6 ou mais caarcteres: ')

    reg_role = 'Jornalista'
    
    Us.create_user(reg_name, reg_username, reg_pass, reg_role)
    reg_sucess_txt()
    Ls.login_txt()



def register_pub_txt():
    print('╔═════════════════╗')
    print('║ Cadastro Leitor ║')
    print('╚═════════════════╝')
   
    reg_name = input('Nome completo: ')
    reg_username = input('Nome de usuário: ')
    
    if Uu.exists_dir(reg_username):
        print('Nome de usuário já está em uso')
        reg_username = input('Tente outro nome de usuário: ')
    
    reg_pass = input('Digite sua senha: ')
    while len(reg_pass) < 6:
        reg_pass = input('Digite uma senha com 6 ou mais caarcteres: ')

    reg_role = 'Leitor'

    Us.create_user(reg_name, reg_username, reg_pass, reg_role)
    reg_sucess_txt()
    Ls.login_txt()
    

def reg_sucess_txt():
    print('╔════════════════════════════════╗')
    print('║ Cadastro realizado com sucesso ║')
    print('╚════════════════════════════════╝')

