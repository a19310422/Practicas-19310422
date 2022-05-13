import random
import numpy as np
from numpy.core.numeric import array_equiv
from networkx.utils.decorators import nodes_or_number
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

data = pd.read_csv('C:\Users\Juan Manuel\Desktop\Aeropuertos.csv')
data.head()

data.set_index(["code"], inplace=True)
data.head()

data.loc["MTY"]

data_vuelos = pd.read_csv("Vuelos_simples.csv")
data_vuelos.head()

data_vuelos.describe()

DG=nx.DiGraph()
for row in data_vuelos.iterrows():
    DG.add_edge(row[1]["origin"],
                row[1]["destination"],
                duration=row[1]["duration"],
                price=row[1]["price"])

    DG.nodes(data=True)

    nx.draw_circular(DG,
                 node_color="lightblue",
                 edge_color="gray",
                 font_size=24,
                 width=2, with_labels=True, node_size=3500,
)
