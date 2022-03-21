#Capitulo 32              
teclado1 = { #inicializamos el diccionario, con "categoria","modelo" y "precio"
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}
teclado1 ={
    "Categoria": "Teclados",
    "Modelo": "HyperX Alloy FPS Pro",
    "Precio": "89,99"
}
for x,y in teclado1.items():#aqui definimos X y Y, X va a momstrar las definiciones, el lado "Izquierdo", y Y va a mostrar sus atributos, y usando la funcion items, obtenemos los valores del diccionario
    print(x," = ",y,".")#se imprime
