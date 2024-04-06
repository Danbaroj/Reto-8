import math

x = float(input("Ingrese el valor de x para la aproximación de la función seno: "))

## Función para calcular la aproximación de la función seno

def aprox_sin(x, n):
    aprox = 0
    for i in range(n):
        aprox += ((-1) ** i) * (((x ** (2 * i + 1)) / (math.factorial(2 * i + 1))))
    return aprox

#Función para encontrar el número de términos necesario para alcanzar el error

def encontrar_n(x, error=0.001):
    n = 1
    diferencia = error + 1  
    while diferencia > error:
        aprox = aprox_sin(x, n)
        seno_real = math.sin(x)
        diferencia = abs(seno_real - aprox) / abs(seno_real)
        n += 1
    return n - 1, aprox, error  # Se devuelve también el valor de error

#Se encargan de llamar a la funcion 

n, aprox, error = encontrar_n(x)  # Se almacena el valor de error retornado por encontrar_n
seno_real = math.sin(x)
diferencia = abs(seno_real - aprox)

print ("Aproximación de la función seno: " + str(aprox)+ ", valor real de la función seno: " + str(seno_real) + ", su diferencia es " +str(diferencia) + " y el valor de n para alcanzar el error de " + str(error) + " : "+ str(n) )