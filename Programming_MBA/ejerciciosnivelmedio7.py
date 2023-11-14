def contar_mayusculas_minusculas(cadena):      
  mayusculas = sum(1 for letra in cadena if letra.isupper())      
  minusculas = sum(1 for letra in cadena if letra.islower())      
  return mayusculas, minusculas
print(contar_mayusculas_minusculas("Soy Sthefano Rivero."))