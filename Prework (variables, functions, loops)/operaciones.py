#Convertir seconds en minutos y segundos
seconds = 1042
display_minutes = 1042 // 60 #la doble barra es para dividir y redondear el resultado hacia abajo.
print(display_minutes) #17 - ya tenemos los minutos

display_minutes2 = 1042 / 60
print(display_minutes2) #17.36666666667 - no sirve en este caso

#Ver el resto
seconds2 = 1042%60
print(seconds2) #sobraron 22 segundos

print(seconds,"segundos son",display_minutes,"minutos y ",seconds2,"segundos.")

first_planet = 149597870 #distancia del sol a la Tierra
second_planet = 778547200 #distancia del sol a Jupiter
#Hallar distancia entre planetas
distancia_km=second_planet-first_planet
print(distancia_km,"km")

distancia_millas=distancia_km//1.609344
print(distancia_millas,"millas")

#Python admite dos tipos principales de números: números enteros (o int) y número de punto flotante (o float)
demo_int = int('215')
print(demo_int)
demo_float = float('215.3')
print(demo_float)

print(abs(39 - 16))
print(abs(16 - 39))

print(round(14.5)) #redondea y devuelve 14. El 0.5 es redondeado hacia abajo en Python.

#Puede optar por redondear siempre hacia arriba al número entero más cercano si usa ceil, o hacia abajo si usa floor (es una biblioteca la que llama a estos comandos)
from math import ceil, floor
round_up = ceil(12.5) #13
print(round_up)
round_down = floor(12.5) #12
print(round_down)

first_planet_input = input('Enter the distance from the sun for the first planet in KM: ')
second_planet_input = input('Enter the distance from the sun for the second planet in KM: ')
first_planet = int(first_planet_input)
second_planet = int(second_planet_input)
distance_km = abs(second_planet - first_planet)
print("La distancia es de: ",distance_km," km.")
