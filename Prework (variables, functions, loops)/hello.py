# Ejecutar un programa (una suma). Además sum es una variable.
sum = 1 + 2
#Función print
print("La suma es:",sum)
print("Show this in the console")
#Creamos la variable producto ejecutando el programa de la multiplicación
product=sum*2
print("Producto:",product)
#Tipos de variables
planets_in_solar_system = 8 # numérica tipo int
distance_to_alpha_centauri = 4.367 # numérica tipo float
can_liftoff = True #booleana
shuttle_landed_on_the_moon = "Apollo 11" #texto, cadena de caracteres o string 
#Ver qué tipo de variable es:
print(type(distance_to_alpha_centauri))

#Operadores
left_side = 10
right_side = 5
a=left_side/right_side
print(a)

#Operadores aritméticos: +,-,*,/
#Operadores de asignación: =, += (incremento de cierto valor), -= (reduciendo de a cierto valor), /=, *=

#Fechas
from datetime import date
fechadehoy=date.today()
print(fechadehoy)    #me devuelve 2023-08-03

#Conversión del tipo de datos: para mostrar por ejemplo un texto y seguido la fecha, convertirla a str
print("Today's date is: " + str(date.today()))
print("Today's date is:",date.today()) #pero también da lo mismo hacerlo así

parsecs=11
lightyears=parsecs*3.26
print(parsecs,"parsecs is",lightyears,"lightyears")

#Entrada de usuario: usuario escribe datos y los pasa al programa. Con función input p/datos del usuario.
print("Welcome to the greeter program")
name = input("Enter your name: ")  #Pide que ponga el nombre y luego hace el saludo.
print("Greetings ",name)

#Función input con números
print("Calculator program")
first_number = input("Write the first number: ")
second_number = input("Write the second number: ")
print(first_number + second_number)  #Devuelve el resultado 34 porque están almacenados como cadenas (text)

#Para hacerlo en numérico usar la función int() que los transforma en números
print(int(first_number) + int(second_number)) #Hace la suma y da el resultado 7

parsecs_input=input("Input number of parsecs:")
parsecs=int(parsecs_input)
lightyears=parsecs*3.26
print (str(parsecs),"parsecs is",str(lightyears),"lightyears")   #str para redondear y dejar como text


