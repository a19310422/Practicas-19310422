import random
import networkx as nx

#Aqui se declaran todos los caballos
c1=random.uniform(5,20); c2=random.uniform(5,20); c3=random.uniform(5,20); c4=random.uniform(5,20); c5=random.uniform(5,20)
c6=random.uniform(5,20); c7=random.uniform(5,20); c8=random.uniform(5,20); c9=random.uniform(5,20); c10=random.uniform(5,20)
c11=random.uniform(5,20); c12=random.uniform(5,20); c13=random.uniform(5,20); c14=random.uniform(5,20); c15=random.uniform(5,20)
c16=random.uniform(5,20); c17=random.uniform(5,20); c18=random.uniform(5,20); c19=random.uniform(5,20); c20=random.uniform(5,20)
c21=random.uniform(5,20); c22=random.uniform(5,20); c23=random.uniform(5,20); c24=random.uniform(5,20); c25=random.uniform(5,20)

#Aqui se declara un arreglo por carrera
print("\n Tiempos de la carrera 1:")
race1=[c1,c2,c3,c4,c5]
race1.sort()
print(race1)

print("\n Tiempos de la carrera 2:")
race2=[c6,c7,c8,c9,c10]
race2.sort()
print(race2)

print("\n Tiempos de la carrera 3:")
race3=[c11,c12,c13,c14,c15]
race3.sort()
print(race3)

print("\n Tiempos de la carrera 4:")
race4=[c16,c17,c18,c19,c20]
race4.sort()
print(race4)

print("\n Tiempos de la carrera 5:")
race5=[c21,c22,c23,c24,c25]
race5.sort()
print(race5)

#Luego se el primer lugar de cada carrera 
pole1 = min(race1)
pole2 = min(race2)
pole3 = min(race3)
pole4 = min(race4)
pole5 = min(race5)

#Se crea un arreglo con los 5 mejores caballos
print("\n Carrera 6:")
race6=[pole1,pole2,pole3,pole4,pole5]
print(race6)

place1 = min(race6)
print(place1)


for x in range(5):
    if place1==race1[x]:
        posi=(race1.index(place1))
        win1=posi+1;
        print("\n El primer lugar es el Caballo:",win1)
        break
    if place1==race2[x]:
        posi=(race2.index(place1))
        win1=posi+6;
        print("\n El primer lugar es el Caballo:",win1)
        break
    if place1==race3[x]:
        posi=(race3.index(place1))
        win1=posi+11;
        print("\n El primer lugar es el Caballo:",win1)
        break
    if place1==race4[x]:
        posi=(race4.index(place1))
        win1=posi+16;
        print("\n El primer lugar es el Caballo:",win1)
        break
    if place1==race5[x]:
        posi=(race5.index(place1))
        win1=posi+21;
        print("\n El primer lugar es el Caballo:",win1)
        break

print("Con un tiempo de:",place1)

race6.sort()
race6.pop(0)
print("\n Carrera 7:",race6)
place2=min(race6)

for x in range(5):
    if place2==race1[x]:
        posi=(race1.index(place2))
        win1=posi+1;
        print("\n El segundo lugar es el Caballo:",win1)
        break
    if place2==race2[x]:
        posi=(race2.index(place2))
        win1=posi+6;
        print("\n El segundo lugar es el Caballo:",win1)
        break
    if place2==race3[x]:
        posi=(race3.index(place2))
        win1=posi+11;
        print("\n El segundo lugar es el Caballo:",win1)
        break
    if place2==race4[x]:
        posi=(race4.index(place2))
        win1=posi+16;
        print("\n El segundo lugar es el Caballo:",win1)
        break
    if place2==race5[x]:
        posi=(race5.index(place2))
        win1=posi+21;
        print("\n El segundo lugar es el Caballo:",win1)
        break

print("Con un tiempo de:",place2)

print("\n Son necesarias 7 carreras para saber cuales son los 2 mejores caballos")


#Para el rafo
Grafo = nx.Graph() # se crea el grafo

#Añadir nodos
Grafo.add_node("Caballo #w1") #El primer lugar
Grafo.add_node("Caballo #w2") #Segundo lugar
Grafo.add_node("Caballo #w3") #3ero
Grafo.add_node("Caballo #w4") #4to
Grafo.add_node("Caballo #w5") #5to


Grafo.add_node("Caballo 2 r1") 
Grafo.add_node("Caballo 2 r2") 
Grafo.add_node("Caballo 2 r3")
Grafo.add_node("Caballo 2 r4")
Grafo.add_node("Caballo 2 r5") 

Grafo.add_nodes_from(["C1.3", "C1.4", "C1.5"])  
Grafo.add_nodes_from(["C2.3", "C2.4", "C2.5"])
Grafo.add_nodes_from(["C3.3", "C3.4", "C3.5"])
Grafo.add_nodes_from(["C4.3", "C4.4", "C4.5"]) 
Grafo.add_nodes_from(["C5.3", "C5.4", "C5.5"]) 

#Añadir aristas
Grafo.add_edge("Caballo #1", "Caballo #2") 

Grafo.add_edge("Caballo #1", "Caballo #3") 
Grafo.add_edge("Caballo #3", "Caballo #4") 
Grafo.add_edge("Caballo #2", "Caballo #5")


Grafo.add_edge("Caballo #1", "Caballo 2 r1") 
Grafo.add_edge("Caballo #2", "Caballo 2 r2")
Grafo.add_edge("Caballo #3", "Caballo 2 r3")
Grafo.add_edge("Caballo #4", "Caballo 2 r4")
Grafo.add_edge("Caballo #5", "Caballo 2 r5")

Grafo.add_edges_from([("Caballo 2 r1", "C1.3"),("C1.3", "C1.4"), ("C1.4", "C1.5")])
Grafo.add_edges_from([("Caballo 2 r2", "C2.3"),("C2.3", "C2.4"), ("C2.4", "C2.5")])
Grafo.add_edges_from([("Caballo 2 r3", "C3.3"),("C3.3", "C3.4"), ("C3.4", "C3.5")])
Grafo.add_edges_from([("Caballo 2 r4", "C4.3"),("C4.3", "C4.4"), ("C4.4", "C4.5")])
Grafo.add_edges_from([("Caballo 2 r5", "C5.3"),("C5.3", "C5.4"), ("C5.4", "C5.5")])

print(len(Grafo.nodes))
print(len(Grafo.edges))
#graficar gafo
nx.draw(Grafo, node_size = 50, width = 1.2, with_labels=True)
plt.show() #mostramos grafo