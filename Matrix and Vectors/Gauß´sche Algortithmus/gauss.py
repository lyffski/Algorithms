import numpy as np
#add the i-ten row of x-factor of j-ten row
#A will be modifly
def rowMod(A, i, j, x): #elementary row mod of type 3 of Matrix
    '''INPUT:= 1: Matrix, i: i-ten row, j: j-ten row, x: factor'''
    #A[i] = A[i] + x * A[j]
    A[i] = [a + x * b for a, b in zip(A[i], A[j])]
    #Output: rowMod(A, 0, 1, 3)
    #mod the A Matrix, add the the 0st row the 3rd row that been multiply by 3

def rowEchelon(A):
    '''Gauss: convert the Matrix to Gauss form (pivot is 1 and under only zeros)'''
    row, col = 0, 0     #start in the 1st row and the first col of the matrix
    rows, cols = len(A), len(A[0])  #get the length of the matrix
    while (row < rows and col < cols):  
        #try to find the pivot
        if (A[row][col]) == 0:
            #iterate the rows under the row-var
            for r in range(row + 1, rows):
                if (A[r][col] != 0): 
                    rowMod(A, row, r, 1)
                    break
        if A[row][col] == 0:
            col += 1
            continue
        pivot = A[row][col]
        for r in range (row + 1, rows):
            if A[r][col] != 0:
                rowMod(A, r, row, -A[r][col]/pivot)
        row += 1
        col += 1

def assign2x2(A):
   '''cast 2x2 Matrix into variables'''
   a, b = A[0][0], A[0][1]
   c, d = A[1][0], A[1][1]
   return a,b,c,d

def assign3x3(A): 
   '''cast 3x3 Matrix into variables'''
   a, b, c = A[0][0],A[0][1],A[0][2]
   d, e, f = A[1][0],A[1][1],A[1][2]
   g, h, i = A[2][0],A[2][1],A[2][2]
   return a,b,c,d,e,f,g,h,i

def arrangeArray(A, cols, rows, decimal):
    '''arrange the values of given list - input:= 1: Array, 2: row, 3: col, 4: decimal'''
    lt = []
    for i in range(rows):
        for j in range(cols):
            A[i][j] = round(A[i][j],decimal)
            lt.append(A[i][j])
    lt = np.array(lt)
    lt = lt.reshape(cols,rows)
    return lt 


A = np.array([[1,0,2], [2,-1,3], [4,1,8]])
iA = arrangeArray(np.linalg.inv(A), 3, 3, 2)
print(iA)


        

