import Util.Util_functions as Uu

directoryUsers = './Users'


def create_user(name, username, password, role):
 
    user = [name, username, password, role] # Guia: [0] = name, [1] = username, [2] = password, [3] = role
    Uu.create_dir(directoryUsers, username) # Cria o diretorio do usuario
    Uu.create_file(directoryUsers + '/' + username + '/', username) # Cria o arquivo do usuario
    Uu.edit_file(directoryUsers + '/' + username + '/' + username + '.txt', user[0] + '\n' + user[1] + '\n' + user[2] + '\n' + user[3])
    Uu.create_dir(directoryUsers + '/' + username, 'News')

    return


def delete_user(username):
   
    Uu.delete_dir(directoryUsers + '/' + username)


def login_user(username, password): # Retorna True se os dados do usuario estiverem corretos   
   
    directory = directoryUsers + '/' + username
    userfile = directory + '/' + username + '.txt'
   
    if Uu.exists_dir(directory) and Uu.ler_arquivo(userfile)[2] == password:
        return True
   
    else:
        return False
    

def get_user(username):
   
    userfile = directoryUsers + '/' + username + '/' + username + '.txt'
    return Uu.ler_arquivo(userfile)


def list_users():
    return Uu.listar_pastas(directoryUsers)