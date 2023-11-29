def valor_absoluto(lista):
 for a in range(len(lista)):
  lista[a] = abs(lista[a])
 return lista 

numeros = [15, -4, 30, -7, 19]
print('Lista con valores absolutos:', valor_absoluto(numeros))
