
def factorial(numero):

  resultado = 1

  for a in range(1,numero+1):
    resultado *= a 
  return resultado 
num = int(input("Ingrese:"))
print("El factorial de", num, "es:", factorial(num))