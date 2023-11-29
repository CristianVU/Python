def suma_cuadrados_pares(n):

   return sum(i**2 for i in range(2, n+1, 2))

print(suma_cuadrados_pares(8))