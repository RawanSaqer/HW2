## create a matrix with size 4 by 7 and the data type integer. Then calculate the mean of the matrix by row
import numpy as np
X=np.random.randint(30, size=(4,7))
print(X)
mean_=np.mean(X,axis=1)
print(mean_)

# one hot vector 
labels=[0,2,4,4,3,3,1,5,5,5,3,1]
u=len(set(labels))
c=len(labels)
arr=np.zeros((u,c))
print(arr)
print()
for ind, i in enumerate(labels):
    ##print(i, ind)
    arr[i,ind]=1
print(arr)

import numpy as np
import time 
import threading

def startCalculation(A,B,no_of_threads):
    block_size=int(A.shape[0]/no_of_threads)
    threads=[]
    blocks=[]
    C=np.zeros_like(A)
    t1=time.time()
    for i in range(no_of_threads):
        b=Block(A,B,i,block_size)
        blocks.append(b)
        t=threading.Thread(target=b.multiplyMatrices)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    for b in blocks:
        C[b.start:b.end,:]=b.C
    t2=time.time()
    print('the time for multiplying two matrics with :',no_of_threads,'=',t2-t1)
    #print(C)



class Block:
    def __init__(self, A, B,idx,block_size):
        self.start=idx*block_size
        self.end=self.start+block_size
        #print(self.start,self.end)
        self.A=A[self.start:self.end,:]
        self.B=B
        self.idx=idx
        self.block_size=block_size
        #print('---------block------------')
        #print(self.A)
        self.C=None
    def multiplyMatrices(self):
        r, c=self.A.shape
        r1,c1=self.B.shape
        self.C=np.zeros((r,c1))

        for i in range(r): 
            for j in range(c): 
                for k in range(c): 
                    self.C[i][j] += self.A[i][k] * self.B[k][j]
        #print('block multiplcation')
        #print(self.C)
        

def createMatrix(m,n):
    return np.random.randint(100,size=(m,n))
    
def multiplyMatrices(A,B):
    r, c=A.shape
    r1,c1=B.shape
    C=np.zeros((r,c1))

    for i in range(r): 
        for j in range(c): 
            for k in range(c): 
                C[i][j] += A[i][k] * B[k][j]
    return C


np.random.seed(2)
m=200
##print(A)
print()
A=createMatrix(m,m)
B=createMatrix(m,m)
threads1=[2,4,8,20]
for t in threads1:
    
    startCalculation(A,B,t)

print()
#C1=np.matmul(A,B)
#print(C1)
