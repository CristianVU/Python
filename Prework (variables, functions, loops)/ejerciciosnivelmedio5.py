def contar_vocales(cadena):     
  
  return sum(1 for letra in cadena if letra.lower() in 'aeiou')  

print(contar_vocales('Hola, como estas?')) 