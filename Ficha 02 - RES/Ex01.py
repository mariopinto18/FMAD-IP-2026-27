"""
Fatorial de um número
nota: fatorial de 0! = 1
"""

numero = int(input("número: "))
# Validar se o numero inserido é negativo. 
# Em caso afirmativo, termina a função
if numero <0:
    print("Não existe fatorial de números negativos!")
    exit()
fatorial = 1       # porque fatoial de 0 é 1  
for i in range(2, numero+1):  # percorre o intervalor de numeros
    fatorial*= i              # entre 2 e o numero inserido
print(f' Fatorial de {numero} é = {fatorial}')