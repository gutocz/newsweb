# Functions of screens in .txt 

# Imports
import Services.Users_services as Us
from Util.Util_functions import ler_arquivo
import Services.News_services as Sn
import Screens.News.News_screen as Ns
import Screens.Register.Register_screen as Rr
import Screens.Menu.Menus_screen as Mm

directoryUsers = '../Users'

def login_txt():
    print('╔═══════════════╗')
    print('║ Menu de login ║')
    print('╚═══════════════╝')
    
    login_username = input('Nome de usuario: ')
    login_pass = input('Senha: ')
    
    if Us.login_user(login_username, login_pass):
       
        if Us.get_user(login_username)[3] == 'Jornalista':
            menu_adm_txt(login_username)
        
        else:
            menu_pub_txt(login_username)
   
    else:
        print('Usuário ou senha inválidos!')
        login_txt()
    
    return Mm.menu_txt()


def log_sucess_txt():
    print('╔═════════════════════════════╗')
    print('║ Login realizado com sucesso ║')
    print('╚═════════════════════════════╝')


def menu_adm_txt(owner):
    print('╔══════════════════════╗')
    print('║  Menu do Jornalista  ║')
    print('╠══════════════════════╣')
    print('║  1 - Criar notícia   ║')
    print('║  2 - Listar notícia  ║')
    print('║  3 - Deletar notícia ║')
    print('║  4 - Editar notícia  ║')
    print('║  5 - Buscar notícia  ║')
    print('║  6 - Sair            ║')
    print('╚══════════════════════╝')
    
    options = input('Selecione uma das opções acima: ')
    match options:
       
        case '1':
            Ns.create_news_txt(owner)
            menu_adm_txt(owner)

        case '2':
            Ns.list_news_txt(owner)
            menu_adm_txt(owner)
      
        case '3':
            Ns.delete_list_txt(owner)
            menu_adm_txt(owner)
       
        case '4':
            Ns.edit_list_txt(owner)
            menu_adm_txt(owner)
       
        case '5':
            #Sn.search_news()
            menu_adm_txt(owner)
       
        case '6':
            Mm.menu_txt()
      
        case _:
            print('Opção inválida.')
            menu_adm_txt(owner)   


def menu_pub_txt(owner):
    print('╔══════════════════════╗')
    print('║    Menu do Leitor    ║')
    print('╠══════════════════════╣')
    print('║ 1 - Buscar notícia   ║')
    print('║ 2 - Listar notícias  ║')
    print('║ 3 - Sair             ║')
    print('╚══════════════════════╝')
  
    options = input('Selecione uma das opções acima: ')
    match options:
      
        case '1':
            Ns.search_screen_txt(owner)
            menu_pub_txt(owner)
       
        case '2':
            print(Sn.list_all_news())
     
        case '3':
            Mm.menu_txt()
       
        case _:
            print('Opção inválida.')
            menu_pub_txt(owner)