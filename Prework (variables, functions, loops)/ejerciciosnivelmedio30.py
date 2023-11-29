def cadena_mas_larga(lista):

  return max(lista, key=len)  

print(cadena_mas_larga(["como", "pasaste", "ayer"]))
