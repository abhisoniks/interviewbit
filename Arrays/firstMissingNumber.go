class Solution:
    def firstMissingPositive(self, A):
        p=max(A)
        if p<=0:
            return 1
        l1=[0]*(p+1)
        for i, val in enumerate(A):
            if val < 0:
                continue
            l1[val]=1
        for i in range(1,len(l1)):
            if l1[i]==0:
                return i
        return p+1
