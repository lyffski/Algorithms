import numpy as np
import networkx as nx

class Node(object):
   '''create a node '''
   def __init__(self, name, conn=None):
      self.name = name
      self.conn = {}
      if conn is not None:
         self.conn.update(conn)

node = [
   Node("A", {"B":1,"C":1}),
   Node("B", {"A":1,"C":0}),
   Node("C", {"A":1,"B":0})
   ]

def shortest_path(start, end):
   P = _dijkstra(start)
   path, node = [], end
   while not (node == start):
      if path.count(node):break
      path.append(node)
      node = P[node]
   return [start] + list(reversed(path))
   
def _dijkstra(start):
   D, P = {},{}
   for nod in node:
      D[nod.name], P[nod.name] = float("inf"), None
   D[start] = 0
   unseen_nodes = list(node)
   while unseen_nodes:
      shortest = min(unseen_nodes, key=lambda node:D[node.name])
      unseen_nodes.remove(shortest)
      for neighbor, distance in shortest.conn.items():
         if neighbor not in [node.name for node in unseen_nodes]:
            continue
         if D[shortest.name] + distance < D[neighbor]:
            D[neighbor] = D[shortest.name]+distance
            P[neighbor] = shortest.name
   return P

 


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


def huffman(L):
   if len(L) <= 2:
      return L
   S = sorted(L, key = lambda pair: pair[1])
   return huffman([[[S[0], S[1]], S[0][1]+S[1][1]]]+ S[2:])

C = huffman([["a", 10], ["b", 15], ["c", 30], ["d", 20], ["e", 25]])


