
def sumar_digitos(numero):
  
 suma = 0
 while numero > 0:
  suma = suma + numero % 10 
  numero = numero// 10
 return suma 
num = int(input("Ingresa el numero:"))
print("la suma de los dígitos es:", sumar_digitos(num))
 