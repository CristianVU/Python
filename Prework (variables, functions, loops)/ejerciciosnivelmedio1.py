def fibonacci(numero):
    
 if numero == 0:  
   return  0 
 elif numero == 1:
    return 1 
 else:
   return fibonacci(numero - 1 ) + fibonacci(numero -2)
num = int(input('Ingrese el numero:'))
print('Los numeros de fibonacci son:')
for a in range(0,num):
 print (fibonacci(a))
 