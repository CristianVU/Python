#Averiguar los divisores de un número
def divisores(numero):
  resultado = [i for i in range (1,numero+1) if numero%i == 0]
  return resultado
n=int(input("Ingrese un número para saber sus divisores :"))
print(divisores(n))

#Crear lista con while
new_planet = ''
planets = []
while new_planet.lower() != 'done':
    if new_planet:
        planets.append(new_planet)
    new_planet = input('Enter a new planet, or done if done:')
print(planets)

#Uso de for en listas
from time import sleep
countdown = [4, 3, 2, 1, 0]
for number in countdown:
    print(number)
    sleep(1)  # Wait 1 second
print("Blast off!! 🚀") #Ha creado una cuenta regresiva de a 1 segundo.

for planet in planets:
    print(planet)


