# File for shape news

# Imports
from email import utils
import Services.News_services as Ns
from Util.Util_functions import *
import Screens.Login.Login_screen as Ls

# Functions for news
# ==================================================================
# Texts of Journalists

# Texts for create news
def create_news_txt(owner):
    print('╔══════════════════╗')
    print('║ CRIE UMA NOTÍCIA ║')
    print('╚══════════════════╝')
    
    title = input('Título: ')
    content = input('Conteúdo: ')
    
    Ns.create_news(owner, title, content, data_atual(), '0', '1')
    create_news_success_txt()


# Texts for list news of users
def list_news_txt(owner):
    print('╔═══════════════════╗')
    print('║ LISTAS DO USUÁRIO ║')
    print('╚═══════════════════╝')
    
    noticias = Ns.list_news(owner)

    for n in noticias:
        print(n + '. ' + Ns.get_news(owner, n)[2])
    
    id_news = input('\nSelecione uma notícia para abrir: \n0- Voltar\n')
    
    if id_news == '0':
        Ls.menu_adm_txt(owner)
    
    else:
        news_choice_txt(owner, id_news)


# Texts for select news
def news_choice_txt(owner, id):
    print('╔═══════════════════════╗')
    print('║  NOTÍCIA SELECIONADA  ║')
    print('╚═══════════════════════╝')
    print(Ns.get_news(owner, id)[2])
    print(len(Ns.get_news(owner, id)[2])*'=')
    print(Ns.get_news(owner, id)[3])
    print('\nAuthor: ' + Ns.get_news(owner, id)[0])
    print('Likes: ' + Ns.get_news(owner, id)[5])
    print('Date of Publish: ' + Ns.get_news(owner, id)[4])
    print(len(Ns.get_news(owner, id)[2])*'=')
    
    option = input('0- Voltar\n1- Deletar noticia\n2- Editar noticia\n')
    match option:
        
        case '0':
            list_news_txt(owner)

        case '1':
            delete_dir(f'./Users' + '/{owner}' + '/News' + '/{id}')

        case '2':
            edit_list_txt(owner)
        
        case _:
                print('Opção inválida.')
                edit_list_txt(owner)

def news_choice_search_txt(owner, id, creator): #creator é quem está acessando a notícia, já owner é o dono
    print('╔═══════════════════════╗')
    print('║  NOTÍCIA SELECIONADA  ║')
    print('╚═══════════════════════╝')
    print(Ns.get_news(owner, id)[2])
    print(len(Ns.get_news(owner, id)[2])*'=')
    print(Ns.get_news(owner, id)[3])
    print('\nAuthor: ' + Ns.get_news(owner, id)[0])
    print('Likes: ' + Ns.get_news(owner, id)[5])
    print('Date of Publish: ' + Ns.get_news(owner, id)[4])
    print(len(Ns.get_news(owner, id)[2])*'=')
    print('Comentários: ')
    #Listando todos os comentários da noticia
    for i in Ns.get_comments(owner, id, creator):
        for j in i:
            print(j)
    
    option = input('0- Voltar\n1- Curtir\n2- Comentar\n')
    match option:
        
        case '0':
            Ls.menu_pub_txt(creator)
        
        case '1':
            Ns.like_news(id, owner, creator)
            news_choice_search_txt(owner, id, creator)
        
        case '2':
            print('Deixe se comentário: ')
            comment = input()
            Ns.comment_news(id, owner, creator, comment)
        
        case _:
                print('Opção inválida.')
                edit_list_txt(owner)


def edit_list_txt(owner):
    
    print('Insira o Id da noticia que deseja editar: ')
    option = input()
    
    if option in Ns.list_news(owner):
        
        print('Selecione o que deseja editar: ')
        option1 = input('0- Título\n1- Conteúdo\n')
        
        match option1:
            
            case '0':
                newtitle = input('Novo título: ')
                Ns.edit_news_title(owner, option, newtitle)
                edit_news_success_txt()
           
            case '1':
                newcontent = input('Novo conteúdo: ')
                Ns.edit_news_content(owner, option, newcontent)
                edit_news_success_txt()

            case _:
                print('Opção inválida.')
                edit_list_txt(owner)
   
    else:
        print('Noticia inexistente')
        Ls.menu_adm_txt(owner)


def delete_list_txt(owner):
    
    print('Insira o Id da noticia que deseja excluir: ')
    option = input()
    
    if option in Ns.list_news(owner):
        Ns.delete_news(owner, option)
        delete_news_success_txt()
    
    else:
        print('Noticia inexistente')
        Ls.menu_adm_txt(owner)

def search_screen_txt(owner):
    
    print('A busca filtrará resultados com base no título da notícia e seu conteúdo')
    term = input('Digite o termo a ser buscado: ')
    result = Ns.search_news(term)
    print('Resultados:\n')
    
    if len(result) == 0:
        print('Nenhuma noticia encontrada')
    
    else:
        
        for r in result:
            print('Título: ' + Ns.get_news(r.split(':')[0], r.split(':')[1])[2] + ' || Autor: ' + Ns.get_news(r.split(':')[0], r.split(':')[1])[0] + ' || Id: ' + r.split(':')[1])
        print('Insira o nome do autor e o id da noticia para visualiza-la')
        nome_autor = input('Autor: ')
        id_noticia = input('Id: ')
        news_choice_search_txt(nome_autor, id_noticia, owner)

# ============================================================================================
# Telas para interação Leitor - Notícias

def list_news_user_txt(creator, owner):
    print('╔═══════════════════╗')
    print('║ LISTAS DO USUÁRIO ║')
    print('╚═══════════════════╝')
    
    noticias = Ns.list_news(owner)

    for n in noticias:
        print(n + '. ' + Ns.get_news(owner, n)[2])
    
    id_news = input('\nSelecione uma notícia para abrir: \n0- Voltar\n')
    
    if id_news == '0':
        Ls.menu_pub_txt(creator)
    
    else:
        news_choice_search_txt(owner, id_news, creator)


# ==================================================================
# Texts of success
def create_news_success_txt():
    print('╔═════════════════════════════╗')
    print('║ NOTÍCIA CRIADA COM SUCESSO! ║')
    print('╚═════════════════════════════╝')


# Text for edit news
def edit_news_success_txt():
    print('╔══════════════════════════════╗')
    print('║ NOTÍCIA EDITADA COM SUCESSO! ║')
    print('╚══════════════════════════════╝')


# Text to delete news
def delete_news_success_txt():
    print('╔═══════════════════════════════╗')
    print('║ NOTÍCIA EXCLUIDA COM SUCESSO! ║')
    print('╚═══════════════════════════════╝')
# ==================================================================
