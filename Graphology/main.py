import numpy as np
import networkx as nx

A = np.array([[0,1,1,1,0],
              [1,0,1,0,0],
              [1,1,0,1,0],
              [1,0,1,0,1],
              [0,0,0,1,0]])

def node_degree(A):
   lt = []
   for j in range (len(A)):
      deg = 0
      for i in range(len(A)):
         if A[i][j] == 1:
            deg += 1
      lt.append(deg)
   return lt

node_deg = node_degree(A)
print(node_deg)

cent = nx.degree_centrality(A)