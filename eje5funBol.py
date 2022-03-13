#Escribir una función que reciba otra función booleana y una lista, y devuelva otra lista
#con los elementos de la lista que devuelvan True al aplicarles la función booleana.

#Se declara la funcion
def funcion_bol(funcion, lista):
    #Se declara la lista 
    lis = []
    #Se recorre la lista para poder aplicar la función
    for i in lista:
        #Se realiza la instrucciòn ya sea el caso que se cumple la condicion es decir sea = True
        if funcion (i):
            lis.append(i)
    return lis
#Se declara la segunda función la cual determina si los valores de la lista son divisibles entre 3
def divisor_tres(n):
    return n % 3 == 0
#Se manda los parametros necesarios tanto de la  primer y segunda función 
print(funcion_bol(divisor_tres, [23,56,23,7,12,8,3,67,2,4,71,5466,87,23]))