def eigenvalue2x2(A): #for 3x3 matrix: -lambda^3 + alpha*lambda^2 + beta*lambda + gamma
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

A = [[3,-1],[1,-1]]
msg = eigenvalue2x2(A)
print(msg)


 