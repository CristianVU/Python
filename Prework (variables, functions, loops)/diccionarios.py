#Python usa las llaves {} y los dos puntos : para crear diccionarios
planet = {
 'name': 'Earth',
 'moons': 1
}
#Se almacenó el nombre del planeta y el número de lunas que tiene. 
#Dos claves: name y moons. Claves se comportan como variables pero están dentro de una variable más grande llamada "planet"
#Se llama a una clave con el término "get" o con []
print(planet.get('name'))
print(planet['name'])
#Si una clave no está disponible, get devuelve "None" y [] devuelve KeyError
wibble = planet.get('wibble') # Returns None
print(wibble)
# wibble = planet['wibble'] # Throws KeyError
#Modificar los valores de un diccionario:
planet.update({'name': 'Makemake'}) #No output: name is now set to Makemake.
planet['name'] = 'Makemake'
print(planet)
#Corchetes es más fácil para valores individuales, pero update permite actualizar varios valores.
planet.update({
    'name': 'Jupiter',
    'moons': 79
})
#Con corchetes se deberían hacer dos llamadas a la función:
planet['name'] = 'Jupiter'
planet['moons'] = 79
#Agregar una clave a un diccionario:
planet['orbital period'] = 4333 #agregamos el período orbital
#Quitar una clave con pop
planet.pop('orbital period')
# planet dictionary now contains: {
#   name: 'jupiter'
#   moons: 79
# }
#Almacenar un diccionario dentro del diccionario planet
# Add address
planet['diameter (km)'] = {
 'polar': 133709,
 'equatorial': 142984
}
#Recuperar valores con diccionario anidado
print(f'{planet["name"]} tiene un diámetro polar en km de: {planet["diameter (km)"]["polar"]}')

#EJERCICIO
planet={
    "name" : "Mars",
    "moons" : 2
    }
print(f'{planet["name"]} has {planet["moons"]} moon(s).')

planet['circunference (km)'] = {
 'polar': 6752,
 'equatorial': 6792
}
print(planet)
print(f'{planet["name"]} tiene una circunferencia polar en km de {planet["circunference (km)"]["polar"]}.')

#El método keys devuelve un objeto de lista que contiene todas las claves
rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
} #Diccionario de precipitaciones de 3 meses en cm
for key in rainfall.keys():
    print(f'{key}: {rainfall[key]} cm')

#Determinar la existencia de una clave determinada en el diccionario para cambiarla o no
if 'december' in rainfall:
    rainfall['december'] = rainfall['december'] + 1
else:
    rainfall['december'] = 2.1
    #Como diciembre ya existe, le sumará 1
print("Los nuevos valores son:")
for key in rainfall.keys():
    print(f' {key}: {rainfall[key]} cm')

#Recuperar todos los valores usando value (devuelve sin sus claves correspondientes)
print("Los valores de precipitaciones de octubre, noviembre y diciembre en cm son respectivamente: ")
for value in rainfall.values():
  print(value) #valores numéricos listados

#Suma total de precipitaciones de esos 3 meses
total=0
for value in rainfall.values():
  total=total+value
print("El total de precipitaciones esos tres meses fue: "+f'{total} cm.')

#EJERCICIO 2
planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}
number_of_moons=planet_moons.values()
number_of_planets=len(number_of_moons)
print("El número total de planetas es: "+f'{number_of_planets}')
total_of_moons=0
for value in number_of_moons:
  total_of_moons=total_of_moons+value
print("El número total de lunas es: "+str(total_of_moons))

promedio_moons=total_of_moons/number_of_planets
print("Cada planeta tiene un promedio de: " +str(promedio_moons)+" lunas.")
