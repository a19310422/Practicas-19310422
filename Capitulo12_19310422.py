#Capitulo 12
color = ['rojo', 'azul', 'verde', 'amarillo', 'marron', 'lila', 'negro', 'rosa', 'blanco', 'naranja'] #Lista de 10 elementos
print("\n\t Lista Original: ", color) #Se imprime la lista

colorlist= color # Asginamos un lista a otra lista
del colorlist[1] #Eliminamos el elemento 1 de la lista
del colorlist[3] #Eliminamos el elemento 3 de la lista
del colorlist[4] #Eliminamos el elemento 4 de la lista
del colorlist[-3] #Eliminamos el elemento -3 de la lista

print("\n\t Lista nueva: ", colorlist) #Imprimimos la nueva lista