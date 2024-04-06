range(1000,1,2)#Secuencia de pares
range(1,1001 )#Secuencia de impares

#Bucle que permite tomar todos los números impares

print("LISTA DE NÚMEROS IMPARES:")
for num in range(1,1001):
    if num % 2 != 0:
        print (num)

#Bucle que permite tomar todos los números pares

print("LISTA DE NÚMEROS PARES:")
for num in range(2,1000,2):
        print(num)