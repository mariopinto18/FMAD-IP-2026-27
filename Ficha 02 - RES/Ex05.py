"""
Ler um numero e indicar de é primo ou não
input: número
Resultado esperado: é primo ou não é primo
"""

numero = int(input("Indique um número: "))
primo = True
for i in range(2,numero):   # teste se nº é divisivel no intervalo 2-numero
    if numero % i == 0:      # numero é divisivel por i
        print(f"o número {numero} não é primo")
        primo = False
        break
# depois do ciclo for
if primo:
    print(f"o número {numero} é primo")
  

