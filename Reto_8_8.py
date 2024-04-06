import math 

x = float(input("Ingrese el valor de x para la aproximación de la función exponencial: "))

# Función para calcular un término de la serie de Maclaurin
def maclaurin(x, n):
    return (x ** n) / math.factorial(n)

# Función para calcular la aproximación de la función exponencial utilizando los n primeros términos de la serie de Maclaurin
def aproximacion_exponencial(x, n):
    aprox = 0
    for i in range(n):
        aprox += maclaurin(x, i)
    return aprox

# Función para determinar el valor de n con menos del 0.1% de error
def encontrar_n(x, error=0.001):
    n = 1  
    diferencia = 1.0 

    #Bucle que busca el numero minimo de terminos de la serie Maclaurin necesarios

    while diferencia > error:
        aprox = aproximacion_exponencial(x, n)
        real_exponencial = math.exp(x)
        diferencia = abs(real_exponencial - aprox) / abs(real_exponencial)
        n += 1
    return n

n = encontrar_n(x)
aprox = aproximacion_exponencial(x, n)
real_exponencial = math.exp(x)
diferencia = real_exponencial - aprox

print ("Aproximación de la función exponencial: " + str(aprox)+ ", valor real de la función exponencial: " + str(real_exponencial) + ", su diferencia es " +str(diferencia) + " y el valor  de n para alcanzar el error de 0.001 : " + str(n) )