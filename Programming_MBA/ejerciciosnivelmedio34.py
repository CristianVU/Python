def contar_vocales(cadena):

  return sum(1 for c in cadena.lower() if c in 'aeiou')

print(contar_vocales("No hay nadie más.")) 