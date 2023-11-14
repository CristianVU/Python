def es_primo(num): 
  if num < 2:
    return False 
  for i in range(2, int(num ** 0.5) + 1): 
    if num % i == 0: 
      return False 
    else:
     return True 
print(es_primo(8))