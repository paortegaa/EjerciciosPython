#Importación de la 
from functools import reduce

#Dada una lista de personas almacenadas en diccionarios: Filtrar de acuerdo con el sexo y
#calcular la media (utilizar reduce y lambda)
#Se crea el diccionario con los datos correspondientes de las personas
lista=[
    {'nombre': 'Paola','edad':20,'sexo':'M'},
    {'nombre': 'Jose','edad':18,'sexo':'H'},
    {'nombre': 'Pedro','edad':17,'sexo':'H'},
    {'nombre': 'Adolfo','edad':15,'sexo':'H'},
    {'nombre': 'Keren','edad':18,'sexo':'M'},
    {'nombre': 'Saul','edad':19,'sexo':'H'}
    
    ]
#Se determinar el filtadro de las personas de sexo femenino
mujeres=list(filter(lambda x: x['sexo']== 'H', lista))
#Se realiza la suma de las edades de las personas femeninas 
suma_edad=reduce(lambda suma, p:suma+p['edad'],mujeres,0)
#Se obtiene la media, dividiendo la suma de las edades de las mujeres entre la cantidad de mujeres que hay en el
#diccionario
media_edad = suma_edad/(len(mujeres))
#Se imprime la media de las edades de las mujeres
print(media_edad)


                

