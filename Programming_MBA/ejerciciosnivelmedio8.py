def es_perfecto(num):      
  return num == sum(divisor for divisor in range(1, num) if num % divisor == 0)   
print(es_perfecto(10)) 