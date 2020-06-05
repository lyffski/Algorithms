def quicksort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    greater_then = []
    smaller_then = []

    for i in sequence:
        if i > pivot:
            greater_then.append(i)

        else:
            smaller_then.append(i)

    return quicksort(smaller_then) + [pivot] + quicksort(greater_then)

print(quicksort([23,11,4,0,2,9,5]))
#the algorithm step by step			middleIndex = (len(sequence) - 1)/2
# [23, 11, 4, 0, 2, 9, 5]   
#    lower [4,0,2] #recursion
#       lower[0]
#          return 0             0 
#       pivot = 2
#          return 2             2
#       greater [4]
#          return 4             4
#    pivot = 5
#       return 5                5
#    grater [23,11,9] #recursion
#       lower[]
#          return None          N 
#       pivot = 9
#          return 9             9
#       greater [23,11] #recursion
#          lower[]
#             return None       N 
#          pivot = 11
#             return 11         11
#          grater [23]
#             return 23         23

#             => [0,2,4,5,N,9,N,11,23] 
#                => [0,2,4,5,9,11,23]

      