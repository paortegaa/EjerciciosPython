#Realizar una función que reciba dos listas y retorne una lista con el contenido de ambas.
#Declaració de las listas 
lista1=['Perro','Gato','Tiburon','cocodrilo','venado']
lista2=['Jirafa','Cebra','Puma','Elefante','Oso']
#Declaración de la lista para unir las listas declaradas
def Agg_lista(lista1,lista2):
    #Creación de una tercera lista para almacenar la union de la lista 1 y 2
    lista3=lista1+lista2
    #retorno de la lista nueva creada
    return lista3
#impresión de la lista 1
print(f"Lista 1: {lista1}")
print("")
#impresión de la lista 2
print(f"Lista 2: {lista2}")
print("")
#impresión de la lista nueva
print(f"Lista con la union de las listas 1 y 2: {Agg_lista(lista1,lista2)}")
            
        
        
    