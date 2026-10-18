
"""
Calcula o IMC (Índice de Massa Corporal)
Ler peso e altura
Imprimir IMC
"""

peso = float(input("Peso (kg):"))
altura =float(input("\nAltura(m):"))

#Calcula o índice de massa corporal, IMC
indiceImc = peso/(pow(altura, 2))

print("\nO seu IMC é: {:.2f}" .format(indiceImc))

