#Ejercicio: Crear una función lambda que permita elevar al cuadrado un valor

#Declaración de la lista
lista=[2,5,6,23,5,2,13]
#Elevación al cuadrado de cada número de la lista creada
elevar_lista=map(lambda x: x**2,lista)
#Impresión a pantalla de la lista obtenida
print(list(elevar_lista))