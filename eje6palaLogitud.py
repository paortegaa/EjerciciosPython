#Escribir una función que reciba una frase y devuelva un diccionario con las palabras que
#contiene y su longitud.

#Se deifne la función la cual recibe una frase como parametro
def longi_palab (frase):
    #Se realiza una lista de las palabras que tiene la frase recibida
    palabras = frase.split()
    #Se realiza el calculo de la cantidad de letras que tienen cada palabra 
    longitud=map(len,palabras)
    #Se retorna en forma de diccionario las palabras de la frase y así mismo la longitud de letras 
    return dict(zip(palabras,longitud))
#Se llama a la función y se pasa el parametro de la frase
print(longi_palab('Sin lluvia no hay flores'))