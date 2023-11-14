def sumar_digitos(numero):
   return sum(int(digito) for digito in str(numero)) 

num = int(input('Ingrese el numero:'))
print('La suma de los digitos es:', sumar_digitos(num))