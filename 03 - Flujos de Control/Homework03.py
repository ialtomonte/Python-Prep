#1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

from pickle import FALSE


var1=3
if (var1>0 or var1<0):
    print(var1)
else:
    print('no imprimir')

#2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

var2='Irene'
var3='ALTOMONTE'

if (type(var2) == type(var3)):
    print('son iguales')
else:
    print('son diferentes') 
#3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar


for n in range(1,21):
    if n % 2 == 0 :
        print ('el numero', str(n) , 'es par')
    else:
        print ('el numero', str(n) , 'es impar')   
    



4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3


for n in range (0,6):
    print('el resultado es' , str(n**3))

5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

#var4=5
#for n in range (1,var4):
#    print('ciclo' , str(n))

n = 12
for i in range(1, n+1):
    print(i)
print ('hice', str(n) , 'ciclos')  


6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

n = 5
factoreo = 1
while (n > 0):
    factoreo=n*factoreo
    n -= 1
print (factoreo)

n = 5
factoreo = 1
if( type(n) == int):
    while (n > 0):
        factoreo=n*factoreo
        n -= 1
    print (factoreo)
else:
    print('no es entero')

#7) Crear un ciclo for dentro de un ciclo while

n = 1
while(n < 5):
    for i in range(1,n+1):
        print('Ciclo for nro ' + str(i))
    print('Ciclo while nro ' + str(n))
    n += 1
      

8) Crear un ciclo while dentro de un ciclo for

n=5
for n in range (1,10):
    while n<5:
        print('ciclo while' , str(n))
        n+=1
    print('ciclo for' , str(n))

n = 5
for i in range(1, n):
    while(n < 5):
        n -= 1
        print('Ciclo while nro ' + str(n))
        print('Ciclo for nro ' + str(i))


9) Imprimir los números primos existentes entre 0 y 30

n = 0
primo = True
while ( n < 31):
    if (n == 0):
        primo = False
    else:
        for div in range (2,n):
            if (n % div == 0):
                primo = False
    if (primo):
        print(str(n) , 'es primo')
    else:
        primo = True
    n += 1

tope_rango=30
n = 0
primo = True
while (n < tope_rango):
    for div in range(2, n):
        if (n % div == 0):
            primo = False
    if (primo):
        print(n)
    else:
        primo = True
    n += 1


#10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

tope_rango=30
n = 0
primo = True
while (n < tope_rango):
    for div in range(2, n):
        if (n % div == 0):
            primo = False
            break
    if (primo):
        print(n)
    else:
        primo = True
    n += 1

11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

contar = 0
tope_rango=30
n = 0
primo = True
while (n < tope_rango):
    for div in range(2, n):
        if (n % div == 0):
            contar += 1
            primo = False
            break
        continue
    if (primo):
        print(n)
    else:
        primo = True
    n += 1
print('bucle' , str(contar))

contar = 0
tope_rango=30
n = 0
primo = True
while (n < tope_rango):
    for div in range(2, n):
        if (n % div == 0):
            contar += 1
            primo = False
    if (primo):
        print(n)
    else:
        primo = True
    n += 1
print('bucle sin break' , str(contar))

#12) Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?

#13) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

n=100
while (n<301):
    n += 1  
    if ( n % 12 != 0):
        continue
    print(n)     

  

#14) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

sigue = 1
n = 0
primo = True
while ( sigue == 1):
    for div in range(2, n):
        if (n % div == 0):
            contar += 1
            primo = False
    if (primo):
        print(n)
        print('¿Desea encontrar el siguiente número primo?')
        if (input() != '1'):
            print('Se finaliza el proceso')
            break
    else:
        primo = True
    n += 1

#15) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

n = 100
while ( n <= 300):
    if ( n % 3 == 0 and type( n*6 == int)):
        print('el número es' ,  str(n))
        break
    n += 1
