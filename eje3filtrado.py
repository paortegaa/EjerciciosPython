#Definición de la lista de mascotas
lista_mascotas = ['Panquesito', 'Negrito', 'Scooby', 'Scrapi', 'Momo', 'Spyque']
#Uso de la función lambda y, la función filter la cual permite agregar a una nueva lista solamente las mascotas llamadas Scooby O Scrapi

print (list(filter (lambda mascota: mascota == 'Scooby' or mascota == 'Scrapi', lista_mascotas)))
