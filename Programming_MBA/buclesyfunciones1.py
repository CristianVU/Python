def es_par(numero):
  return numero % 2 == 0 
num = int(input("Ingrese un numero:"))
if es_par(num):
 print('Es un numero par')
else:
  print ('Es un numero impar')
