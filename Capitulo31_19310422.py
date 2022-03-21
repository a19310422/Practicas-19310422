#Capitulo 31           
teclado1 = { #inicializamos el diccionario, con "categoria","modelo" y "precio", con su respectivo valor
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}
teclado2 = {
    "Categoria": "Teclados",
    "Modelo": "Corsair K55 RGB",
    "Precio": "59,99"
    }
consulta = teclado2["Modelo"]#se obtiene el valor en la posicion modelo
consulta2 =teclado2["Precio"]#se obtiene el valor en la posicion precio
print("El modelo",consulta,"cuesta",consulta2, "$")#Se imprime la concatenacion
