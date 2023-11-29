from collections import Counter

def elemento_mas_comun(lista):

     return Counter(lista).most_common(1)[0][0]

print(elemento_mas_comun([28, 27, 28, 11, 78, 2, 7]))