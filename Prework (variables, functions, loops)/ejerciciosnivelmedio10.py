def interseccion(list1, list2):      
  
  return list(set(list1) & set(list2))   

print(interseccion([22, 15, 125, 18], [18, 15, 45, 79]))