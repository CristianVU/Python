

def primo(a):
 if a == 1:
   return("no_primo")
 for b in range(2, a):
   if a % b == 0 :
    return("no_primo")
   else:
     return("es_primo") 

print(primo(10))