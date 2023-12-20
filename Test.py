from Services.Users_services import *
from Services.News_services import *

#create_user('Gustavo', 'gutocz', '123', 'admin')
#delete_user('gutocz')

#create_news('gel', 'fabula', 'froid', '26/05', '34', 1)

#print(login_user('gutocz', '123'))

#print(get_news('gutocz', 3489)[3])

resultado_busca = search_news('queijo')
for i in resultado_busca:
    print(i.split(':'))
