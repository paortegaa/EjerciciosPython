#Escribir una función que reciba otra función y una lista, y devuelva otra lista con el
#resultado de aplicar la función dada a cada uno de los elementos de la lista.
#Se define la funcion principal la cual recibe otra función y un lista
def aplicar_funcion(funcion, lista):
    #Se declara la lista 
    lis = []
    #Se recorre la lista para poder aplicar la función
    for i in lista:
        lis.append(funcion(i))
    return lis
#Se declara la segunda función la cual realizará la suma de una unidad a cada uno de los elementos de la lista
def funcion_sumar(n):
    return n + 1
#Se manda los parametros necesarios tanto de la  primer y segunda función 
print(aplicar_funcion(funcion_sumar, [2,435,7,2,6,8,21,6,2,56]))
    