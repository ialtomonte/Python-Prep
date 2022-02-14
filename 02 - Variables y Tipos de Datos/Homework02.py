# 1) Crear una variable que contenga un elemento del conjunto de números 
# enteros y luego imprimir por pantalla
entero=3
print(entero) 
# 2) Imprimir el tipo de dato de la constante 8.5
type(8.5)

#3) Imprimir el tipo de dato de la variable creada en el punto 1
type(entero)

#4) Crear una variable que contenga tu nombre
myname="Irene"

#5) Crear una variable que contenga un número complejo
complejo=1+3j

#6) Mostrar el tipo de dato de la variable crada en el punto 5
type(complejo)

# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

pi=3.1416

# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

var2="True"
var3=True

# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9

type(var2)
type(var3)
# 10) Asignar a una variable, la suma de un número entero y otro decimal
var4=10
var5=0.2

var6=var4+var5
print(var6)
# 11) Realizar una operación de suma de números complejos

var7=10+5j
var8=5+5j
print(var7+var8)

# 12) Realizar una operación de suma de un número real y otro complejo
p
rint(10+10+20j)

#13) Realizar una operación de multiplicación

print(5*5)

#14) Mostrar el resultado de elevar 2 a la octava potencia
print(2**8)

#15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

var9=27/4
print(var9)

#16) De la división anterior solamente mostrar la parte entera

var10=27//4
print(var10)

#17) De la división de 27 entre 4 mostrar solamente el resto

var11=27%4
print(var11)

#18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

var10*4+var11

#19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
 
var1="soy "
var2="Irene"

print(var1+var2)

#20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
 
 2=="2"

#porque evalua si es V o F

#21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
type(2)
2==int("2")


#22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

a = float('3,8')
#porque no reconoce la coma como decimal

#23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido

var12=3
var12-=1
print(var12)

#24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

1<<2

#25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

#los 2 operandos deben ser del mismo tipo
 # si son integrales
 print(2+2)
 # si son caracter
 print("2"+"2")

#26) Realizar una operación válida entre valores de tipo entero y string

var1 = 'este texto se repite '
var2 = 3
print(var1 * var2 + str(var2) + ' veces')