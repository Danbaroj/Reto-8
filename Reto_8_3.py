#Numero n dado
limite=int(input("Ingrese un número natural mayor o igual a 2: "))
range(1000,1,-2)#Numeros pares desde el 1000 hasta el 2

#Bucle para tomar los valores menores o iguales al numero n dado

for num in range(1000,1,-2):
    if num <= limite:
        print (num)