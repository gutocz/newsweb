# Functions for screens in txt

# Imports
import Screens.Register.Register_screen as Reg
import Screens.Login.Login_screen as Log

# ==================================================================
# Texts for menus
def web_txt():
    print('╔══════════════════╗')
    print('║ Site de Notícias ║')
    print('╚══════════════════╝')


def menu_txt():
    print('╔════════════════╗')
    print('║ Menu Principal ║')
    print('╠════════════════╣')
    print('║  1 - Cadastrar ║')
    print('║  2 - Logar     ║')
    print('║  3 - Sair      ║')
    print('╚════════════════╝')
   
    options = input('Selecione uma das opções acima: ')
    match options:
     
        case '1':
            Reg.register_txt()
            Reg.adm_or_pub_txt()
        
        case '2':
            Log.login_txt()

       
        case '3':
            exit()
       
        case _:
            print('Opção inválida.')
            menu_txt()        
# ==================================================================
