class Solution:
    # @param A : list of integers
    # @return an integer
    def bulbs(self, A):
        flip=0
        i=0
        while i<len(A):
            if A[i]==0:
                if flip%2==0:
                    flip+=1
                while i<len(A) and A[i]==0:
                    i+=1
                continue
            else:
                if flip%2==1:
                    flip+=1
                while i<len(A) and A[i]==1:
                    i+=1
                continue
            i+=1
        return flip
