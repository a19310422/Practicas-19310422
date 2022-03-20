#Capitulo 16
colors = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja'] 
print("\n Lista Original: ", colors) #Imprimimos la lista 
colors.insert(6, 'magenta') #Se añade el elemento magenta en la posicion 6, la cual en realidad sera la 7 
colors.insert(-1, 'turquesa') #Se añade el elemento magenta en la posicion -1, la cual en realidad sera la -2 
print("\n Lista nueva: ",colors) #Imprimos la nueva lista