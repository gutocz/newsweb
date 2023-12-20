# File for useful functions

# Imports
import os
import shutil
from datetime import datetime

def exists_dir(caminho): # Função que verifica se um diretório existe
    return os.path.exists(caminho)


# Cria o diretório se ele não existir
def create_dir(caminho, namedir): # Funcao que cria um diretorio, recebe o local onde deve ser criado e nome do mesmo
    
    if not os.path.exists(caminho + '/' + namedir):
        os.makedirs(caminho + '/' + namedir)
    
    else:
        raise ValueError('Diretório Inválido')
    

def create_file(caminho, namefile): # Funcao que cria um arquivo, recebe o local onde deve ser criado e nome do mesmo
    
    if not os.path.exists(caminho + '/' + namefile):
        open(caminho + '/' + namefile + '.txt', 'w')
    
    else:
        raise ValueError('Arquivo Inválido')
    

def edit_file(caminho, content): # Função que edita um arquivo, recebe o local e o conteudo
    
    with open(caminho, 'w') as f:
        f.write(content)


def delete_dir(caminho): # Funcao que deleta um diretorio e tudo que estiver dentro dele
    
    if os.path.exists(caminho):
        shutil.rmtree(caminho)
    
    else:
        raise ValueError('Diretório Inexistente')


def ler_arquivo(caminho):
    
    # Abre o arquivo em modo de leitura ('r')
    with open(caminho, 'r') as arquivo:
      
        # Lê as linhas do arquivo e as armazena em uma lista
        linhas = arquivo.readlines()
        # Remove caracteres de quebra de linha (\n) de cada linha e retorna a lista
        return [linha.strip() for linha in linhas]


def listar_arquivos(caminho):
   
    # Verifica se o caminho da pasta existe
    if os.path.exists(caminho):
      
        # Obtém uma lista de todos os arquivos e pastas no caminho especificado
        lista_arquivos = os.listdir(caminho)

        # Itera sobre a lista para filtrar e exibir apenas os arquivos
        arquivos = [excluir_ultimos_digitos(str(arquivo)) for arquivo in lista_arquivos if os.path.isfile(os.path.join(caminho, arquivo))]

        return arquivos
   
    else:
        print("O caminho especificado não existe.")
        return []


def listar_pastas(caminho):
   
    # Verifica se o caminho da pasta existe
    if os.path.exists(caminho):
      
        # Obtém uma lista de todos os arquivos e pastas no caminho especificado
        lista_pastas = os.listdir(caminho)

        # Itera sobre a lista para filtrar e exibir apenas as pastas
        pastas = [str(pasta) for pasta in lista_pastas if os.path.isdir(os.path.join(caminho, pasta))]

        return pastas
    
    else:
        print("O caminho especificado não existe.")
        return []


def excluir_ultimos_digitos(palavra):
    #return palavra[:-4]
    return palavra

def data_atual():
    
    # Obtém a data e hora atuais
    data_atual = datetime.now()

    # Converte a data atual em uma string formatada
    data_atual_str = data_atual.strftime("%Y-%m-%d %H:%M:%S")
    return data_atual_str
