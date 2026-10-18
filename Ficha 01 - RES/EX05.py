"""
Ler um número inteiro.
Imprimir se é par ou ímpar. 
cálculo: auando dividido por 2, se er resto 0, é par. Senão é ímpar. 
"""

number = int(input("Indique um número: "))
if number %2 == 0:    # resto da divisão = 0 => é par
    print("O número {:n} é par" .format(number))
else:
    print("O número {:n} é ímpar" .format(number))
