def elementos_no_comunes(lista1, lista2):

  return list(set(lista1) ^ set(lista2))

print(elementos_no_comunes([18, 19, 20, 21], [21, 22, 23, 24]))