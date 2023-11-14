def divisores(num):

  return [a for a in range(1, num + 1) if num% a == 0]

print(divisores(10))