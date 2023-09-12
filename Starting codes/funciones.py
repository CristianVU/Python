def rocket_parts():
    print("payload, propellant, structure")
rocket_parts()
#Se puede asignar la salida de la función a una variable
output=rocket_parts()
print(output) #Devuelve None porque la función no ha devuelto un valor

#Hacer que la función devuelva una cadena
def rocket_parts():
  return "payload, propellant, structure"
output=rocket_parts()
print(output)

#Función any: toma un objeto iterable (por ejemplo, una lista) y devuelve True si algún elemento del objeto iterable es True. De lo contrario, devuelve False.
output=any([True, False, False])
print(output) #True
output=any([False, False, False])
print(output)

#Función str: convierte el argumento en una cadena, si no se le da un argumento, devuelve cadena vacía
print(str())
print(str(15))

#Funciones con argumento
def distance_from_earth(destination):
    if destination == "Moon":
        return "238.855 km"
    else:
        return "Unable to compute to that destination."
print(distance_from_earth("Moon"))
print(distance_from_earth("Mars"))

def days_to_complete(distance, speed):
    hours = distance/speed
    return (hours/24)
resultado=days_to_complete(30000,20)
resultado=round(resultado)
print(resultado,"días para completar ese viaje.")
print(round(days_to_complete(376464,285)),"días para completar ese viaje.")

def generate_report(main_tank,external_tank,hydrogen_tank):
 return f"Fuel report: \n Main tank: {main_tank} \n External tank: {external_tank} \n Hydrogen tank: {hydrogen_tank}"
print(generate_report(10,20,30))

#Argumentos de palabra clave (son argumentos opcionales, requieren valor predeterminado)
from datetime import timedelta, datetime
def arrival_time(hours): #poner la duración del viaje en horas
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime("Arrival: %A %H:%M")
print(arrival_time(51))
print(arrival_time(256))

#Combinación de argumentos y argumentos de palabra clave
from datetime import timedelta, datetime
def arrival_time(destination, hours=51): #se fija un argumento por defecto
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime(f"{destination} Arrival: %A %H:%M")
print(arrival_time("Moon"))
print(arrival_time("Orbit", hours=0.13))

#Argumentos de variable
def variable_length(*args): 
    print(args)
# *args indica a la función que acepte cualquier número de argumentos (incluido 0)
variable_length()
variable_length("one", "two")
variable_length(None)

#Vamos a crear una función de longitud variable que pueda calcular cuántos minutos quedan hasta el inicio, dado el tiempo que va a tardar cada paso:
def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f"Total time to launch is {total_minutes} minutes"
    else:
        return f"Total time to launch is {total_minutes/60} hours"
print(sequence_time(4, 14, 18)) #Resultado es la suma de los 3 números: 36minutos
print(sequence_time(4, 14, 48)) #Ahora lo da en horas

#Argumentos de palabra clave variable: se usa doble asterisco
def variable_length(**kwargs):
    print(kwargs)

variable_length(tanks=1, day="Wednesday", pilots=3) #los argumentos de palabra clave de longitud variable se asignan como un diccionario.

#En esta función, vamos a usar argumentos de palabra clave variable para notificar los astronautas asignados a la misión.
def crew_members(**kwargs):
    print(f"{len(kwargs)} astronauts assigned for this mission:")
    for title, name in kwargs.items():
        print(f"{title}: {name}")

crew_members(captain="Neil Armstrong", pilot="Buzz Aldrin", command_pilot="Michael Collins")
#las palabras clave deben ser distintas. No se puede poner por ejemplo dos veces pilot

#EJERCICIO
def fuel_report(**fuel_tanks):
  for title,name in fuel_tanks.items():
    print(f'{title}:{name}')
fuel_report(main=50, external=100, emergency=60)

