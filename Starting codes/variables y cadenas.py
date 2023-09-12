#CONDICIONALES
a = 16
b = 30
c = 27
if a > b and a > c:
 print ("a es el máximo")
elif b > c and b > a:
    print ("b es el máximo")
else:
    print ("c es el máximo")

object_size = 10
proximity = 9000

if object_size > 5 and proximity < 1000:
    print('Evasive maneuvers required')
else:
    print('Object poses no threat')
    
#CADENAS (STRINGS)
fact = "The Moon has no atmosphere."
fact2 = fact + " No sound can be heard on the Moon."
print(fact2)

multiline = "Facts about the Moon:\n There is no atmosphere.\n There is no sound."
print(multiline)
print("temperatures and facts about the moon".title()) #pone en mayus la primera de c/palabra

heading = "lo mismo se produce almacenando como variable"
heading_upper = heading.title()
print(heading_upper)

#División de una cadena
temperatures = "Daylight: 260 F Nighttime: -280 F"
temperatures_list = temperatures .split()
print(temperatures_list)

temperatures = "Daylight: 260 F\n Nighttime: -280 F"
temperatures_list = temperatures .split('\n')
print(temperatures_list)

#Búsqueda de una palabra en una cadena (true or false)
print("Moon" in "This text will describe facts and challenges with space travel") #FALSE
print("Moon" in "This text will describe facts about the Moon") #TRUE

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.find("Moon")) #devuelve -1 cuando no se encuentra la palabra

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.find("Mars")) #64 es la posición donde empieza esa palabra en la cadena

#Contar veces que aparece una palabra
temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.count("Mars"))
print(temperatures.count("Moon"))

print("The Moon And The Earth".lower())
print("The Moon And The Earth".upper()) #TODAS LAS LETRAS A MAYÚSCULAS

temperatures = "Mars Average Temperature: -60 C"
parts = temperatures.split(':') #para texto regular
print(parts)
print(parts[-1]) #Devuelve el último elemento

#para texto irregular
mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
    if item.isnumeric():
        print(item) #Devuelve 30, sólo sirve para positivos. con isdecimal lo mismo para decimales

#Detectar un número negativo porque empieza con guión (-)
print("-60".startswith('-')) #TRUE (primer caracter de una cadena)

if "30 C".endswith("C"):
 print("This temperature is in Celsius") #Evaluar con qué termina una cadena


