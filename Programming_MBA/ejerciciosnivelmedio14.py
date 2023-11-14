def filtrar_palabras(lista_de_palabras, n):

   return [palabra for palabra in lista_de_palabras if len(palabra) > n]

print(filtrar_palabras(["Estoy", "eliptico", "comarca", "amor"], 4)) 