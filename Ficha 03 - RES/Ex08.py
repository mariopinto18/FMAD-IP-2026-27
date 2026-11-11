#reverseWords - recebe um texto e inverte a ordem das palavras

def reserveWords(texto):
    """
    Recebe um texto e devolve o mesmo texto com palavras por ordem inversa  
    Args: texto: string
    return: string: texto por ordme inversa 
    """

    listaPalavras =  texto.split(" ")   # dividir o texto pelos espaços
    textoReverse = listaPalavras[::-1]  # inverter a ordem da lista de palavras
    result=""                           # Result - o texto por ordem inversa
    for palavra in textoReverse:        # percorrer a lista de palavras
        result+= palavra + " "          # juntar as palavras da lista, concatenando um espaço 
    return result.rstrip()              # renmove o ultimp espaço do texto
    
texto = input("Insira o Texto: ")
print(reserveWords(texto))