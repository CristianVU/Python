def numero_primo(numero):
  if numero == 1 :
    return 'No es primo'
  for a in range(2, numero):
   if numero%  a == 0:
    return 'No es primo'
   else: 
     return 'Es primo'

num = int(input('Ingrese el numero:'))
print('Este numero es:', numero_primo(num))