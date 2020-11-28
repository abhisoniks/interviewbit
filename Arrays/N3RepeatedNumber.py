class Solution:
    def repeatedNumber(self, A):
        count1=[ A[0], 1 ]
        count2=[ "", 0 ]
        count3=[ "", 0 ]
        for i in range(1,len(A)):
            val=A[i]
            if val == count1[0]:
                count1[1]+=1
                continue
            if val == count2[0]:
                count2[1]+=1
                continue
            if val == count3[0]:
                count3[1]+=1
                continue
            if count2[0]=="" or count2[1]<=0:
                count2=[val,1]
                continue
            if count3[0]=="" or count3[1]<=0:
                count3=[val, 1]
                continue
            count1[1]-=1
            count2[1]-=1
            count3[1]-=1
            if count1[1]<=0:
                count1=[val, 1 ]
                continue
            if count2[1]<=0:
                count2=[ val, 1]
                continue
            if count3[1]<=0:
                count3=[ val, 1]
                continue
        n = len(A)
        n1=count1[0]
        n2=count2[0]
        n3=count3[0]

        countA=0
        countB=0
        countC=0
        for i in A:
            if i==n1:
                countA+=1
                continue
            if i==n2:
                countB+=1
                continue
            if i==n3:
                countC+=1
                continue


        if countA > int(n/3):
            return n1
        if countB > int(n/3):
            return n2
        if countC > int(n/3):
            return n3
        return -1
        
