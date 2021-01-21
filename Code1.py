


from numpy import *
import numpy as np
import time
import threading 



class Blocck:
    def __init__(self, size):
        self.size = size
    def multiplyMatrices(self,A,B):
        
        r, c=A.shape
        r1,c1=B.shape
        C=np.zeros((r,c1))

        for i in range(r): 
            for j in range(c): 
                 for k in range(c): 
                    C[i][j] += A[i][k] * B[k][j]
        return C
    def two(self, size):
        seed = np.random.seed(1)
        A = np.random.randint(0,size, size=(size,size))
        B = np.random.randint(0,size, size=(size,size))
        print("\n")
        print(A)
        one = array(A[:,0:int(size/2)])
        two = array(A[:,int(size/2):size])
        t1 =self.multiplyMatrices(one,B)
        t2 =self.multiplyMatrices(two,B)
        print("result 1",t1,"\n")
        print(    "result 2",    t2)
       
    def four(self,size):
        seed = np.random.seed(1)
        A = np.random.randint(0,size, size=(size,size))
        B = np.random.randint(0,size, size=(size,size))
        print("4")
        one =array(A[:,0:int(1/4*size)])
        two = array(A[:,int(1/4*size):int(2/4*size)])
        three =array(A[:,int(2/4*size):int(3/4*size)])
        four = array(A[:,int(3/4*size):size])
        f1 = self.multiplyMatrices(one,B)
        f2= self.multiplyMatrices(two,B)
        f3 =self.multiplyMatrices(three,B)
        f4 = self.multiplyMatrices(four,B)
        print("result \n",f1)
        print("result \n",f2)
        print("result \n",f3)
        print("result \n",f4)
        
                

    
    def six(self,szie):
        seed = np.random.seed(1)
        A = np.random.randint(0,size, size=(size,size))
        B = np.random.randint(0,size, size=(size,size))
        
        one_6 =array(A[:,0:int(1/6*size)])
        two_6 =array(A[:,int(1/6*size):int(2/6*size)])
        three_6 =array(A[:,int(2/6*size):int(3/6*size)])
        four_6= array(A[:,int(3/6*size):int(4/6*size)])
        five_6 =array(A[:,int(4/6*size):int(5/6*size)])
        six_6 = array(A[:,int(5/6*size):size])
        s1 = self.multiplyMatrices(one_6,B)
        s2 = self.multiplyMatrices(two_6,B)
        s3 = self.multiplyMatrices(three_6,B)
        s4 = self.multiplyMatrices(four_6,B)
        s5 = self.multiplyMatrices(five_6,B)
        s6 = self.multiplyMatrices(six_6,B)
        print("result \n",s1)
        print("result \n",s2)
        print("result \n",s3)
        print("result \n",s4)
        print("result \n",s5)
        print("result \n",s6)
    
    def eight(self,size):
        seed = np.random.seed(1)
        A = np.random.randint(0,size, size=(size,size))
        B = np.random.randint(0,size, size=(size,size))
        
        one_8 =array(A[:,0:int(1/8*size)])
        two_8 =array(A[:,int(1/8*size):int(2/8*size)])
        three_8 =array(A[:,int(2/8*size):int(3/8*size)])
        four_8= array(A[:,int(3/8*size):int(4/8*size)])
        five_8 =array(A[:,int(4/8*size):int(5/8*size)])
        six_8 = array(A[:,int(5/8*size):int(6/8*size)])
        seven_8 = array(A[:,int(6/8*size):int(7/8*size)])
        eigth_8 = array(A[:,int(7/8*size):size])
        s1 = self.multiplyMatrices(one_8,B)
        s2 = self.multiplyMatrices(two_8,B)
        s3 = self.multiplyMatrices(three_8,B)
        s4 = self.multiplyMatrices(four_8,B)
        s5 = self.multiplyMatrices(five_8,B)
        s6 = self.multiplyMatrices(six_8,B)
        s7 = self.multiplyMatrices(seven_8,B)
        s8 = self.multiplyMatrices(eigth_8,B)
        print("result \n",s1)
        print("result \n",s2)
        print("result \n",s3)
        print("result \n",s4)
        print("result \n",s5)
        print("result \n",s6)
        print("result \n",s7)
        print("result \n",s8)
        
        
        print(" eight")
    
    def ten(self,size):
        seed = np.random.seed(1)
        A = np.random.randint(0,size, size=(size,size))
        B = np.random.randint(0,size, size=(size,size))
        print("from 10")
        t_1 =array(A[:,0:int(1/10*size)])
        t_2 =array(A[:,int(1/10*size):int(2/10*size)])
        t_3 =array(A[:,int(2/10*size):int(3/10*size)])
        t_4 =array(A[:,int(3/10*size):int(4/10*size)])
        t_5 =array(A[:,int(4/10*size):int(5/10*size)])
        t_6 =array(A[:,int(5/10*size):int(6/10*size)])
        t_7 =array(A[:,int(6/10*size):int(7/10*size)])
        t_8 =array(A[:,int(7/10*size):int(8/10*size)])
        t_9 =array(A[:,int(8/10*size):int(9/10*size)])
        t_10 =array(A[:,int(9/10*size):size])
        m1 = self.multiplyMatrices(t_1,B)
        m2 = self.multiplyMatrices(t_2,B)
        m3 = self.multiplyMatrices(t_3,B)
        m4 = self.multiplyMatrices(t_4,B)
        m5 = self.multiplyMatrices(t_5,B)
        m6 = self.multiplyMatrices(t_6,B)
        m7 = self.multiplyMatrices(t_7,B)
        m8 = self.multiplyMatrices(t_8,B)
        m9 = self.multiplyMatrices(t_9,B)
        m10 = self.multiplyMatrices(t_10,B)
        print("result \n",m1)
        print("result \n",m2)
        print("result \n",m3)
        print("result \n",m4)
        print("result \n",m5)
        print("result \n",m6)
        print("result \n",m7)
        print("result \n",m8)
        print("result \n",m9)
        print("result \n",m10)
        
        
    
    def twelve(self,size):
        seed = np.random.seed(1)
        A = np.random.randint(0,size, size=(size,size))
        B = np.random.randint(0,size, size=(size,size))
        print("12")
        
        v1 = array(A[:,0:int(1/12*size)]) 
        v2 = array(A[:,int(1/12*size):int(2/12*size)]) 
        v3 = array(A[:,int(2/12*size):int(3/12*size)]) 
        v4 = array(A[:,int(3/12*size):int(4/12*size)])
        v5 = array(A[:,int(4/12*size):int(5/12*size)]) 
        v6 = array(A[:,int(5/12*size):int(6/12*size)])
        v7 = array(A[:,int(6/12*size):int(7/12*size)])
        v8 = array(A[:,int(7/12*size):int(8/12*size)]) 
        v9 = array(A[:,int(8/12*size):int(9/12*size)]) 
        v10 = array(A[:,int(9/12*size):int(10/12*size)])
        v11 = array(A[:,int(10/12*size):int(11/12*size)]) 
        v12 = array(A[:,int(11/12*size):size])
        m1 = self.multiplyMatrices(B,v1)
        m2 = self.multiplyMatrices(B,v2)
        m3 =self.multiplyMatrices(B,v3)
        m4 = self.multiplyMatrices(B,v4)
        m5 = self.multiplyMatrices(B,v5)
        m6 = self.multiplyMatrices(B,v6)
        m7 = self.multiplyMatrices(B,v7)
        m8 = self.multiplyMatrices(B,v8)
        m9 = self.multiplyMatrices(B,v9)
        m10 = self.multiplyMatrices(B,v10)
        m11 = self.multiplyMatrices(B,v11)
        m12 = self.multiplyMatrices(B,v12)
        print("result \n",m1)
        print("result \n",m2)
        print("result \n",m3)
        print("result \n",m4)
        print("result \n",m5)
        print("result \n",m6)
        print("result \n",m7)
        print("result \n",m8)
        print("result \n",m9)
        print("result \n",m10)
        print("result \n",m11)
        print("result \n",m12)
        
        
    def calculation(self,size, number):

        
        if number ==2:
            #print("from2")
            self.two(size)
         
        
          
        elif number ==4:
            self.four(size)
        
        
           
          
        elif number == 6:
            self.six(size)
            
        elif number ==8:
            self.eight(size)
            
            
        elif number==10:
            self.ten(size)
            
        elif number == 12:
            self.twelve(size)

### Calculating the time that the full of matrix spends during the multiplication process

#list to select from the no
collection =[2,4,6,12]
#loop to create 4 division type (2,4,6,12)
for i in collection:
    Block = Blocck(120)
    t1 = time.time()
    Z=threading.Thread(target=Block.calculation, args=(120,i,)) 
    Z.daemon = True
    Z.start()
    total = time.time() -t1
    print(total)







### Calculating the time when we divided the matrix into 2,4,6,12 


seed = np.random.seed(1)
A = np.random.randint(0,1200, size=(1200,1200))
B = np.random.randint(0,1200, size=(1200,1200))
tt1 = time.time()
C= np.matmul(A,B)
tt2 = time.time()
spend = tt2-tt1
print(spend)


CC1=np.matmul(A,B)
print(CC1)

res=np.sum(np.subtract(C,CC1))
print(res)
