import math

x = float(input("Ingrese el valor de x en el rango [-1, 1]: "))

#Función para aproximar la función arcotangente

def aprox_arctan(x, n):

    aprox = 0

    #Repetir sobre los primeros n términos de la serie de Maclaurin

    for i in range(n):
        aprox += (((-1) ** i) * ((x ** (2 * i + 1)) / (2 * i + 1)))
    return aprox

error = 0.001

n = 1

#Bucle encargado de repetirse hasta que la diferencia entre la aproximación y el valor real sea menor que el margen de error

while True:
    aprox = aprox_arctan(x, n)
    arct_real = math.atan(x)
    diferencia = abs(aprox - arct_real)

    if diferencia < error:
        break

    n += 1

print ("Aproximación de la función Arcotangente es: " + str(aprox)+ ", valor real de la función seno: " + str(arct_real) + ", su diferencia es " +str(diferencia) + " y el valor de n para alcanzar el error de " + str(error) + " : "+ str(n) )