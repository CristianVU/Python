def serie_fibonacci(n):      
  if n <= 0:          
    return []      
  elif n == 1:          
    return [0]      
  fib = [0, 1]      
  while len(fib) < n:          
    fib.append(fib[-1] + fib[-2])      
    return fib   
print(serie_fibonacci(7))