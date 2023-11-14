def suma_acumulada(lista):

 total = 0 
 suma_acumulada = []
 for numero in lista:
    total += numero
    suma_acumulada.append(total)
 return suma_acumulada
print(suma_acumulada([1, 2, 3, 4, 5]))