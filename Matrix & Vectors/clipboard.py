import numpy as np

def evQuadratic(A):
   '''solve the eigenwert using Quadratic Equations''' 
   a,b,c,d = cast2x2(A)
   disc = (((a+d)/2) ** 2) - a*d + b*c
   if disc < 0:
      msg = "Solutionset do not exist, since the discrimant is negative" 
      return msg
   disc = disc ** 0.5
   if disc >= 0:
      evp = ((a+d)/2 + disc)
      evn = ((a+d)/2 - disc)
      return evp, evn #if the disc have been irrational => substract the evalues

def cast2x2(A):
   '''cast 2x2 Matrix into variables'''
   a, b = A[0][0], A[0][1]
   c, d = A[1][0], A[1][1]
   return a,b,c,d

def cast3x3(A): 
   '''cast 3x3 Matrix into variables'''
   a, b, c = A[0][0],A[0][1],A[0][2]
   d, e, f = A[1][0],A[1][1],A[1][2]
   g, h, i = A[2][0],A[2][1],A[2][2]
   return a,b,c,d,e,f,g,h,i


A2 = np.array([[3,-1],[1,1]])
A3 = np.array([[5,-1,2],[-1,5,-2],[2,2,2]])
msg = evQuadratic(A2)


# Ax = b == x = Ab^-1
   # A = np.array([[3,-9],[2,4]])
   # b = np.array([-42,2])
   # x = np.linalg.solve(A,b)

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
ghb


from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

dataset = {"k":[[1,2],[2,3],[3,1]], "r":[[6,5],[7,7],[8,6]]}
new_features = [4,1]

def k_nearest_neighbor(data, predict, k=3):
   distance = []
   for group in data:
      for features in data[group]:
         euclidean_dist = np.linalg.norm(np.array(features)-np.array(predict))
         distance.append([euclidean_dist, group])
   pulls = [i[1] for i in sorted(distance)[:k]]
   print(Counter(pulls).most_common(1))
   pull_result = Counter(pulls).most_common(1)[0][0]
   return pull_result

result = k_nearest_neighbor(dataset, new_features, k=3)
print(result)

[[plt.scatter(ii[0],ii[1], s=100, color=i) for ii in dataset[i]] for i in dataset]
plt.scatter(new_features[0],new_features[1], s=50, color=result)
plt.show()