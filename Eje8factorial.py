#Realizar una función que calcule la factorial de un número

#Se pide ingresar el número para calcular el factorial 
numero = int(input("Ingrese un número para obtener el factorial: "))
#Se define la función factorial
def factorial (numero):
    #Inicialización de la variable
    gr = 1
    if numero >=1:
        #Condición para multiplicar hasta el número indicado por teclado
        for i  in range(1,numero+1):
            gr = gr * i
        #Retorno del resultado de la función     
        return gr
#Impresión del resultado al realizar el llamado a la función 
print(f"El factorial de {numero} es: {factorial(numero)}")