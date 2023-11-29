def ordenar_por_ultimo_elemento(tuplas):

  return sorted(tuplas, key=lambda x: x[-1])

print(ordenar_por_ultimo_elemento([(5, 7), (8, 6), (9, 1)])) 