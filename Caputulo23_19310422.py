#Capitulo 23
age = int(input('¿Cuál es tu edad?\n')) #Pide la edad al usuario
if age <= 0: #Si la edad es menor o igual que 0 se ejecuta el if
	print('Nadie puede tener esa edad.')

elif age <= 1 and age < 18: #si esta entre 1 y 18, ejecuta el elif e imprime que es menor de edad
	print('Eres menor de edad.')

elif age == 18 and age <= 45: #si tiene entre 18 y 45, se imprime que es mayor de edad
	print('Eres mayor de edad.')

elif age <= 100:  #si tiene menor a 100 años, se imprime el mensaje siguiente
	print('Eres mayor de edad.') 

elif age > 100 and age <= 120: #y si tiene entre 100 y 120, imprime lo siguiente
	print('Persona con edad muy avanzada.')

else: #de ser ninguno el caso, ya sea un numero negativo o mayor a 120, imprime edad no valida
	print('Edad no válida.')
