n= int(input("Ingrese un número natural: ")) #Exponente de x 
x = int(input("Ingrese un número real: ")) #Número al que se le va a sacar la potencia
potencia = 1

#Bucle encargado de multiplicar x la cantidad de veces que se le den a la variable "n"

for poten in range(n):
    potencia *= x

print(str(x) + " elevado al numero " + str(n) + " da como resultado " + str(potencia)) 