#Capitulo 24
entrada = input('Introduce el color:\n')#El usuario ingresa el color a buscar
tupla = ("rojo","azul","verde","negro")#declaramos la tupla

if entrada in tupla:#si el color buscado esta dentro, corre la tupla
    print('Color admitido')
else:#de ser lo contrario se ejecuta el else
    print('El color que buscas no está')
