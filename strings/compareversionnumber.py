class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def compareVersion(self, A, B):
        i=0
        j=0
        partitionA=A.split(".")
        partitionB=B.split(".")
     #   print(len(partitionA))
        if len(partitionA) == len(partitionB) and len(partitionA)==1:
            if int(A)<int(B):
                return -1
            elif int(A)>int(B):
                return 1
            else:
                return 0
        equal=abs(len(partitionA)-len(partitionB))
        if equal==0:
            equal=len(partitionA)
        for i in range(equal):
    #        print(int(partitionA[i]),"",int(partitionB[i]))
            if int(partitionA[i])<int(partitionB[i]):
                return -1
            if int(partitionA[i])>int(partitionB[i]):
                return 1


        pA=len(partitionA)
        pB=len(partitionB)
        flag=False
        if pA==pB:
            if int(partitionA[-1])<int(partitionB[-1]):
                return -1
            elif int(partitionA[-1])>int(partitionB[-1]):
                return 1
            else:
                return 0
        pToCheck= ""
        if pA>pB:
            pToCheck=partitionA
        else:
            pToCheck=partitionB
            flag=True
        for i in range(equal,len(pToCheck)):
            if int(pToCheck[i])!=0:
                if flag:
                    return -1
                return 1
        return 0
