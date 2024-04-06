limite = int(input("Ingrese un número natural: ")) #Número natural n, que limitara la lista
range(limite+1)#Numeros desde 0 hasta el numero n
factorial= 1

#Bucle para sacarle factorial a cada numero hasta el número n

for num in range(limite+1):

    #Bucle que se encargará de fatorizar cada número

    for x in range(1, num + 1 ):
        factorial *= x
    print("El factorial de " + str(num) + " es " + str(factorial))
    
    factorial = 1#Se encarga de reiniciar el factorial para los proximos números