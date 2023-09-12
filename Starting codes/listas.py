planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print("The first planet is", planets[0])
print("The second planet is", planets[1])
print("The third planet is", planets[2])

#Cambiar un elemento de la lista
planets[3] = "Red Planet"
print(planets)
print("Marte is known as",planets[3])

number_of_planets = len(planets) #largo de una cadena
print("There are", number_of_planets, "planets in the solar system.")

#Agregar un elemento a una lista
planets.append("Pluto")
number_of_planets = len(planets)
print("There are actually", number_of_planets, "planets in the solar system.")

planets.pop() #pop quita el último elemento
number_of_planets = len(planets)
print("There are actually", number_of_planets, "planets in the solar system.")

#índices negativos para empezar a contar desde el final de la lista
print("The last planet is", planets[-1])
print("The penultimate planet is", planets[-2])

#Búsqueda de valor en una lista con index
jupiter_index = planets.index("Jupiter")
print(jupiter_index) #Lugar que ocupa jupiter en la lista, hay que corregirlo +1.
print("Jupiter is the", jupiter_index + 1, "planet from the sun")

gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
bus_weight = 12650 # in kilograms, on Earth
print("On Earth, a double-decker bus weighs", bus_weight, "kg")
print("On Mercury, a double-decker bus weighs", bus_weight * gravity_on_planets[0], "kg")
print("The lightest a bus would be in the solar system is", bus_weight * min(gravity_on_planets), "kg")
print("The heaviest a bus would be in the solar system is", bus_weight * max(gravity_on_planets), "kg")

#Segmentación de listas
planets_before_earth = planets[0:2]
print(planets_before_earth)
planets_after_earth = planets[3:] #sin poner nada va hasta el final de la lista
print(planets_after_earth)

#Unir nuevamente las listas
planets2=planets_before_earth+planets_after_earth
print(planets2) #lista sin la tierra

#Ordenar listas con sort (orden alfabético)
planets2.sort()
print(planets2)

planets2.sort(reverse=True) #ordenar en order invertido
print(planets2)

user_planet = input("Please enter the name of the planet (with a capital letter to start): ")
planet_index = planets.index(user_planet)
print(planets)
print(planet_index)
print("Here are the planets closer than " + user_planet + ":")
print(planets[0:planet_index])

print(planets)
print(planets[-1]) #último lugar de la lista