#Escribir una función que realice el calculo del seno de un número y retorne el resultado
#Se hace el uso de la libreria math, el cual referido a calculos matematicos
import math
#Se pide al usuario que ingrese un valor
seno= int(input ("Ingresa el valor a calcular: "))
#Se le asigna a la variable alor el valor de math.sin que es referido al seno y entre parentesis el número que se calculará el seno
valor= math.sin(seno)
#Seimprime a pantalla el valor de seno del número dado
print (f'El seno es:  {valor} ')
    