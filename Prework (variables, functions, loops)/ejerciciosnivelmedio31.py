def es_primo(num): 

 if num < 2:
    return False
 else:
   for i in range(2, int(num ** 0.5) + 1): 
    if num % i == 0: 
     return False 
    else:
     return True

def primeros_n_primos(n):
  primos = []
  numero = 2
  while len(primos) < n:
    if es_primo(numero):
      primos.append(numero)
    numero += 1
  return primos

print(primeros_n_primos(5))