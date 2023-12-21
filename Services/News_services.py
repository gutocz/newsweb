import Util.Util_functions as Uu
import Services.Users_services as Us

directoryUsers = './Users'

def create_news(owner, title, content, date, likes, id):

    if not Uu.exists_dir(directoryUsers + '/' + owner + '/News' + '/' + str(id) + '/' + str(id) + '.txt'):
      
        news = [owner, str(id), title, content, date, likes] # Guia: [0] = owner, [1] = id, [2] = title, [3] = content, [4] = date, [5] = likes
        Uu.create_dir(directoryUsers + '/' + owner + '/News/', str(id))
        Uu.create_file(directoryUsers + '/' + owner + '/News/' + str(id), str(id))
        Uu.create_dir(directoryUsers + '/' + owner + '/News/' + str(id), 'Comments')
        Uu.edit_file(directoryUsers + '/' + owner + '/News/' + str(id) + '/' + str(id) + '.txt', news[0] + '\n' + news[1] + '\n' + news[2] + '\n' + news[3] + '\n' + news[4] + '\n' + news[5])
    
    else:
        newid = int(id) + 1
        create_news(owner, title, content, date, likes, str(newid))
    

def get_news(owner, id):
    
    newsDirectory = directoryUsers + '/' + owner + '/News' + '/' + str(id)
    newsData = Uu.ler_arquivo(newsDirectory + '/' + str(id) + '.txt')
    return newsData


def list_news(owner):
    
    directory = directoryUsers + '/' + owner + '/News'
    return Uu.listar_pastas(directory)


def delete_news(owner, id):
    
    Uu.delete_dir(directoryUsers + '/' + owner + '/News' + '/' + str(id))


def edit_news_title(owner, id, newtitle):
    
    news = get_news(owner, id)
    news[2] = newtitle
    Uu.edit_file(directoryUsers + '/' + owner + '/News/' + id + '/' + id + '.txt', news[0] + '\n' + news[1] + '\n' + news[2] + '\n' + news[3] + '\n' + news[4] + '\n' + news[5])


def edit_news_content(owner, id, newcontent):
    
    news = get_news(owner, id)
    news[3] = newcontent
    Uu.edit_file(directoryUsers + '/' + owner + '/News/' + id + '/' + id + '.txt', news[0] + '\n' + news[1] + '\n' + news[2] + '\n' + news[3] + '\n' + news[4] + '\n' + news[5])
    

def search_news(termo):
    
    # Verifica se o termo está no titulo de uma noticia ou no conteudo
    result = []
   
    for user in Us.list_users():

        if Uu.exists_dir(directoryUsers + '/' + user + '/News'):
      
            for id in list_news(user):
                news = get_news(user, id)
                
                if termo.lower() in news[2].lower() or termo.lower() in news[3].lower():
                    result.append(str(news[0]) + ':' + str(news[1])) # Guia: [0] = owner, [1] = id
    
    return result


def like_news(id, owner, who_liked):
    
    news = get_news(owner, id)

    if not Uu.exists_dir(directoryUsers + '/' + who_liked + '/' + 'posts_liked.txt'):
        Uu.edit_file(directoryUsers + '/' + who_liked + '/' + 'posts_liked.txt', owner + ':' + id + '\n')
        news[5] = str(int(news[5]) + 1)
        Uu.edit_file(directoryUsers + '/' + owner + '/News/' + id + '/' + id + '.txt', news[0] + '\n' + news[1] + '\n' + news[2] + '\n' + news[3] + '\n' + news[4] + '\n' + news[5])
    
    else:
        print('Voce ja curtiu essa noticia!')
    


def comment_news(id, owner, creator, comment):
   
    if not Uu.exists_dir(directoryUsers + '/' + owner + '/News/' + id + '/Comments/' + creator + '.txt'):
        Uu.edit_file(directoryUsers + '/' + owner + '/News/' + id + '/Comments/' + creator + '.txt', creator + ' - ' + comment + '\n')
   
    else:
        Uu.add_line(directoryUsers + '/' + owner + '/News/' + id + '/Comments/' + creator + '.txt', creator + ' - ' + comment)

def get_comments(owner, id, creator):
    result = []
   
    if creator != '':
      
        for usuario in Uu.listar_arquivos(directoryUsers + '/' + owner + '/News/' + id + '/Comments'):
            temp = Uu.ler_arquivo(directoryUsers + '/' + owner + '/News/' + id + '/Comments/' + usuario + '.txt')
            result.append(temp)
  
    return result

def list_all_news():
    directoryUsers = './Users/'
    result = []
    
    users = Uu.listar_pastas(directoryUsers)
  
    for user in users:
        news = Uu.listar_pastas(directoryUsers + user + '/News')
       
        for new in news:
            result.append(get_news(user, new))
   
    return result