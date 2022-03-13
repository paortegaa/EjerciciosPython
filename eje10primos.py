#Realice una función que reciba una lista y determine si los elementos dentro de la lista
#son número primos lo que resulten serlo deben mostrarse en una nueva lista.

#Se define la funcion la cual recibe la lista

def num_primos(lis):
    #Se define la lista de los números primos 
    primos = []
    #Se recorre la lista recibida
    for i in lis:
        
        #Se inicializa un contador
        p = 0
        
        #Sea el caso que uno de los números de la lista sea igual a 1 este se agrega automaticamente a la lista de números primos
        if i == 1:
          primos.append(i)
          #Sea lo contrario se comienza a obtener los números del 1 al número que se va obteniendo de la lista 
        else:
          for j in range(1,i+1):
              #Se realiza las divisiones para dterminar que el número sea primo
              if i % j == 0:
                  #Se incrementa el contador sea el caso
                  p += 1
          #Se crea la condicion que determinará que el número es primo solamente cuando se divide entre 1 y entre el mismo
          #Por ello el contador debe ser igual a 2, y así se agregan a la lista de primos
          if p == 2:              
            primos.append(i)
    #Se retorna la lista de primos        
    return primos
#Se declara la lista
lista = [3,56,34,76,76,36,8,32,53,9,12,4,1, 8,4,23,87,12,24,97,64,83]

#Se llama a la función y se pasa el parametro de la lista
print(num_primos(lista))
            
