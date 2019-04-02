import numpy as np
def printmat(matrix) :
    for i in range(3): 
        for j in range(3): 
            print(matrix[i][j], end = " ") 
        print() 

matrix = [] 
print("Enter the entries row-wise:") 
  
for i in range(3):
    a =[] 
    for j in range(3):      
         a.append(int(input())) 
    matrix.append(a) 

printmat(matrix)

pivot=matrix[1][1]
mask=[[128,64,32],[1,0,16],[2,4,8]]

printmat(mask)


comp = np.zeros((3,3))
comp = comp.astype(int)
for i in range(3):
    for j in range(3):   
        if matrix [i][j] >= pivot:
            comp[i][j]=1
        else:
            comp[i][j]=0
            
printmat(comp)

result=comp*mask

printmat(result)