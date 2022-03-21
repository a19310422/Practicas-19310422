#Capitulo 35
def colores(*args):#definimos la funcion args
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')#imprimimos los valores que se mandaron

colores('rojo', 'azul', 'verde', 'amarillo')#mandamos los diferentes valores
colores('lila', 'negro', 'rojo')
colores('rosa','negro')
colores('marrón', 'naranja')

def suma(*args): #Definimos la función 
	resultado = args[0] + args[1] + args[2] + args[3] + args[4] #Realizamos la suma de acuerdo a la posición 
	print('El resultado de sumar estos cinco números es:', resultado) 
suma(5, 7, 45, 8657, 3, 4)
