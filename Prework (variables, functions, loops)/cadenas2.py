#Transformación de texto utilizando cadenas
text="Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."

print(text)

sentences = text.split('. ')
print(sentences)

for sentence in sentences:
    if 'temperature' in sentence:
        print(sentence)
        
#INTRODUCIR VARIABLES EN UNA CADENA
mass_percentage = "1/6"
print("On the Moon, you would weigh about %s of your weight on Earth." % mass_percentage)
print("Both sides of the %s get the same amount of sunlight, but only one side is seen from %s because the %s rotates around its own axis when it orbits %s." % ("Moon", "Earth", "Moon", "Earth"))

mass_percentage = "1/6"
print("On the Moon, you would weigh about {} of your weight on Earth.".format(mass_percentage))

mass_percentage = "1/6"
print("You are lighter on the {0}, because on the {0} you would weigh about {1} of your weight on Earth.".format("Moon", mass_percentage))

mass_percentage = "1/6"
print("You are lighter on the {moon}, because on the {moon} you would weigh about {mass} of your weight on Earth.".format(moon="Moon", mass=mass_percentage))

#Cadenas f-string: empezar la cadena con f y así las variables pueden ir entre corchetes
print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth.")
print(f"On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth.")

subject = "interesting facts about the moon"
heading = f"{subject.title()}" #transformar en título haciendo mayúsculas las primeras letras
print(heading)

subject = "interesting facts about the moon"
heading = f"{subject.title()}"
print(heading)

name = 'Ganymede'
planet = 'Mars'
gravity = '1.43'
print(name)

template="Gravity Facts about {name}\n------------------------------------\nPlanet Name: {planet}\nGravity on {name}: {gravity} m/s2 "
print(template)

print(template.format(name=name,planet=planet,gravity=gravity))