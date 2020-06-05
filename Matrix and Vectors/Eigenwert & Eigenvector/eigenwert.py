def eigenwert(A): 
   a = A[0][0]
   b = A[0][1]
   c = A[1][0]
   d = A[1][1]
   disc = ((((a+d)/2) ** 2) - a*d + b*c) ** 0.5
   if disc < 0:
      print("Solutionset do not exist")
   if disc == 0:
      eigenwert = ((a+d)/2 + disc)
      print("L = {" + str(eigenwert) + "}")
   if disc > 0:
      eigenwert = ((a+d)/2 + disc)
      eigenwertN= ((a+d)/2 - disc)
      print("L = {" + str(eigenwert) +";"+ str(eigenwertN) + "}")


A = [[3,-1],[1,-1]]
eigenwert(A)

 