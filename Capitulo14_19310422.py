#Capitulo 14
colors = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja'] 
print("\n\t Lista Original", colors) #Imprimimos la lista 

color1 = colors.pop(3) #Se elimina el elemento 1 de la lista y se guarda en la variable colorslist
color2 = colors.pop(5)#Se elimina el elemento 7 de la lista y se guarda en la variable colorslist

delatecolors = [color1, color2] #Guardamos en una nueva lista las variables de nuestros elementos borrados de la lilsta anterior
print("\n\t Colores eliminados: ",delatecolors) #Imprimimos los colores eliminados

