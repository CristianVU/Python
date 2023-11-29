def tienen_comun(lista1, lista2):

   return bool(set(lista1) & set(lista2))

print(tienen_comun([17, 18, 19], [19,  20, 21])) 