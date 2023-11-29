def contar_digitos_letras(cadena):

 digitos = sum(c.isdigit() for c in cadena)

 letras = sum(c.isalpha() for c in cadena)

 return digitos, letras

print(contar_digitos_letras("Hola, es la casa 13")) 