exponente= int(input("ingrese un número: ")) #Exponente de 2
potencia = 1

#Bucle encargado de multiplicar 2 la cantidad de veces que se le den a la variable "exponente"

for poten in range(exponente):
    potencia *= 2

print("2 elevado al numero" + str(exponente) + " da como resultado " + str(potencia)) 