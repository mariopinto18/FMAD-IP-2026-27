"""
Dados o limite inferior e limite superior,
calcular a soma de todos os números pares nesse intervalo  
"""

# Ler limite inferior e superior do intervalo
limInf = int(input("Indique o limite inferior: "))
limSup = int(input("Indique o limite superir: "))

if limInf > limSup:    # valida os limites inf e sup introduzidos 
    print("O limite inferior tem que ser menor que o limite superior!!")
    exit()

soma=0
if limInf %2 != 0:   # verificar se limInf é par. 
    limInf+1         # se não for, soma 1 ao limInf (para ser par)
for i in range (limInf, limSup+1, 2):  # Percorrer números no intervalo
           soma+=i
print(f"A soma é {soma}")