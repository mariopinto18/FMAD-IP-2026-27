import random


def generatePassword(userName):
    """
    Gera e devolve uma password, baseada no userName\n
    Args: userName string
    Returns: string com password gerada
    """
    if userName.count(" ") != 0:             # se contar espaços, então inválido
        print("User Name inválido")
        return
    password = ""
    for i in range(len(userName)):          # Percorre todos os caracteres do userName
        if i % 2 == 0:                      # verifica se o caracter está numa posição par
            password+= str(random.randint(1,9))  # gerar nº aleatorio 1-9
        else:
            password+= userName[i]          # guarda na password o próprio caracter do username    
    lista = "#!_-&*"                        # lista caracteres especiais
    password+= lista[random.randint(0,5)]   # acrescenta uma posição aleatória da lista
    password+= str(len(userName))           # acrescenta o nº caracteres username (length)
    return password                         # devolve a password gerada
            

# Arranque do meu programa
userName= input("Indique o seu nome: ")
print(generatePassword(userName))