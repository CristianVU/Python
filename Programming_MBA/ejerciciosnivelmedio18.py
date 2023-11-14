def segundo_maximo(lista):

   return sorted(set(lista), reverse=True)[1]

print(segundo_maximo([58, 37, 21, 13, 8, 99]))