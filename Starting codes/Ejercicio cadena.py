#Crear lista y dar número n, para devolver los n primeros elementos de la lista
def primerosvalores(lista,n):
 return lista[0:n]
valor=""
list=[]
valor=input("Ingresar de a un valor (FIN para finalizar):")
while valor!="FIN":
    list.append(valor)
    valor=input("Ingresar valor (FIN para finalizar):")
num=int(input("Ingresar un número entero:"))

print(primerosvalores(list,num))