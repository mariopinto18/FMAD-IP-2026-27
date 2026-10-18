""" 
Converte temperatura de ºCelsius para º Fahrenheit
forma de conversão: ºF = 1.8 * ºC + 32
"""
tempCelsius = float(input("Temperatura em ºCelsius: "))
tempFahrenheit = 1.8* tempCelsius +32

# Imprime o valor da temperatura convertido em ºFarenheit
print("Temperatura em ºFahrenheit {:.2f} ºF " .format(tempFahrenheit))

