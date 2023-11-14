
def encontrar_maximo(lista):

    maximo = lista[0]

    for numero in lista:
      if numero > maximo: maximo = numero 
    return maximo
 
numeros = [1,7,154,78,25]
print('El numero maximo es:', encontrar_maximo(numeros))