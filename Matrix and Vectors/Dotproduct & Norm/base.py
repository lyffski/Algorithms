import numpy as np



def arcOf2Vectors(v, u):
    '''Create dotproduct of given vertices'''
    v = v
    u = u
    alpha = dot(v,u) / ((dot(v,v)**0.5) * (dot(u,u)**0.5))
    print(alpha)
    x = np.arccos(alpha) 
    print(x)
   
def dot(v, u):
    dot = 0
    for i in range(len(v)):
        dot += v[i] * u[i]
    return dot
        
        

v = np.array([2,2,1])
u = np.array([1,1,0])

arcOf2Vectors(v,u)

