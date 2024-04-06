## Reto-8

1. Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.
```python
range(1,101)# Genera la secuencia de numeros desde el 1 hasta el 100

for num in range (1,101):
    #Primero imprime cada numero que se encuentre en la secuencia y luego imprime su cuadrado
    print(str(num)+" su cuadrado es el número " + str(num**2))
```
2. Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.
```python
range(1000,1,2)#Secuencia de pares
range(1,1001 )#Secuencia de impares

#Bucle que permite tomar todos los números impares

print("LISTA DE NÚMEROS IMPARES:")
for num in range(1,1001):
    if num % 2 != 0:
        print (num)

#Bucle que permite tomar todos los números pares

print("LISTA DE NÚMEROS PARES:")
for num in range(2,1001,2):
        print(num)
```
3. Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado
```python
#Numero n dado
limite=int(input("Ingrese un número natural mayor o igual a 2: "))
range(1000,1,-2)#Numeros pares desde el 1000 hasta el 2

#Bucle para tomar los valores menores o iguales al numero n dado

for num in range(1000,1,-2):
    if num <= limite:
        print (num)
```
4. Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial
```python
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
```
5. Calcular el valor de 2 elevado a la potencia n usando ciclos for.
```python
exponente= int(input("ingrese un número: ")) #Exponente de 2
potencia = 1

#Bucle encargado de multiplicar 2 la cantidad de veces que se le den a la variable "exponente"

for poten in range(exponente):
    potencia *= 2

print("2 elevado al numero " + str(exponente) + " da como resultado " + str(potencia)) 
```
6. Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for. Disclaimer: Trate de no utilizar el operador de potencia (**).
```python
n= int(input("Ingrese un número natural: ")) #Exponente de x 
x = int(input("Ingrese un número real: ")) #Número al que se le va a sacar la potencia
potencia = 1

#Bucle encargado de multiplicar x la cantidad de veces que se le den a la variable "n"

for poten in range(n):
    potencia *= x

print(str(x) + " elevado al numero " + str(n) + " da como resultado " + str(potencia)) 
```
7. Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.
```python
range(1,11) #Números del 1 a 10
primero = 1 #Número base que se va multiplicar con los números del 1 al 10
numeros = 1
print("Tabla del 1:") 

#Bucle encargado de multiplicar la variable "primero" con los números del 1 al 10

for uno in range(1,11):
    uno *=primero 
    print("1 X " + str(numeros)+ " = " +str(uno) )
    numeros += 1 


segundo = 2
numeros =1 
print("Tabla del 2:")

#Bucle encargado de multiplicar la variable "segundo" con los números del 1 al 10

for dos in range(1,11):
    dos *=segundo 
    print("2 X " + str(numeros)+ " = " +str(dos) )
    numeros += 1 

tercero = 3
numeros = 1 

#Bucle encargado de multiplicar la variable "tercero" con los números del 1 al 10

print("Tabla del 3:")
for tres in range(1,11):
    tres *=tercero 
    print("3 X " + str(numeros)+ " = " +str(tres) )
    numeros += 1 

cuarto = 4
numeros =1 
print("Tabla del 4:")

#Bucle encargado de multiplicar la variable "cuarto" con los números del 1 al 10

for cuatro in range(1,11):
    cuatro *=cuarto 
    print("4 X " + str(numeros)+ " = " +str(cuatro) )
    numeros += 1 

quinto = 5
numeros =1 
print("Tabla del 5:")

#Bucle encargado de multiplicar la variable "quinto" con los números del 1 al 10

for cinco in range(1,11):
    cinco *= quinto 
    print("5 X " + str(numeros)+ " = " +str(cinco) )
    numeros += 1 

sexto = 6
numeros =1 
print("Tabla del 6:")

#Bucle encargado de multiplicar la variable "sexto" con los números del 1 al 10

for seis in range(1,11):
    seis *= sexto 
    print("6 X " + str(numeros)+ " = " +str(seis) )
    numeros += 1

septimo = 7
numeros = 1 
print("Tabla del 7:")

#Bucle encargado de multiplicar la variable "septimo" con los números del 1 al 10

for siete in range(1,11):
    siete *= septimo 
    print("7 X " + str(numeros)+ " = " +str(siete) )
    numeros += 1

octavo = 8
numeros = 1
print("Tabla del 8:")

#Bucle encargado de multiplicar la variable "octavo" con los números del 1 al 10

for ocho in range(1,11):
    ocho *= octavo
    print("8 X " + str(numeros) + " = " + str(ocho))
    numeros += 1

noveno= 9
numeros = 1
print("Tabla del 9:")

#Bucle encargado de multiplicar la variable "noveno" con los números del 1 al 10

for nueve in range(1,11):
    nueve *= noveno
    print("9 X " + str(numeros) + " = " + str(nueve))
    numeros += 1
```
8. Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. **Nota:** use *math* para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación.
$$e^x \approx exp(x,n) \approx \sum_{i=0}^{n}\frac{x^i}{i!}$$
```python
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
```
9. Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. **Nota:** use *math* para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.
$$sin(x) \approx sin(x,n) \approx \sum_{i=0}^{n} (-1)^i \frac{x^{2i+1}}{(2i+1)!}$$
```python
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
```
10. Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin. **Nota:** use *math* para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación.
$$arctan(x) \approx arctan(x,n) \approx \sum_{i=0}^{n} (-1)^i \frac{x^{2i+1}}{(2i+1)}$$
```python
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
```
