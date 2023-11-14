def signo_del_numero(numero):
 if numero == 0:
    return 'cero'
 elif numero > 0 :
    return 'positivo'
 else:  
    return "Negativo"
num = int(input('Ingrese el numero:'))
print("El signo del numero es:", signo_del_numero(num))