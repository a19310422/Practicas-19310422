#Capitulo 13
colors = ['rojo', 'azul', 'verde', 'amarillo', 'marron', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
print("\n\t Lista de colores original: ", colors) #Imprimimos la lista original

colorsnew= colors #Se le asigna la lista colrs a otra lista

colorsnew.remove('amarillo') #Con el metodo remove, se elimina el elemneto amarillo de la lista
colorsnew.remove('rojo') #Con el metodo remove, se elimina el elemneto rojo de la lista

print("\n\t Nueva lista : ", colorsnew) #Imprimimos la lnueva lista
