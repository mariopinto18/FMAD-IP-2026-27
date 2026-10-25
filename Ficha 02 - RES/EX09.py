"""
Ler n número e determinar o segundo maior
input: quantidade de números a ler; números
resultado: obter o segundo maior
"""

qt = int(input("Quantos númeos deseja ler? "))

maximo = 0
segundoMaior = 0
for i in range(qt):
    numero = int(input(f"{i+1}º Número:"))
    if numero > maximo:     # determina o maior de um conjunto de numeros
        segundoMaior= maximo
        maximo= numero
    elif  numero == maximo:
        continue
    elif numero > segundoMaior:
        segundoMaior = numero

print(f'\n\n\t\tThe second biggest number is: {segundoMaior}' )
  
    
