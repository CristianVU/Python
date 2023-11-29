def contar_caracteres(cadena):

   return {caracter: cadena.count(caracter) for caracter in cadena}

print(contar_caracteres("Todos los días."))