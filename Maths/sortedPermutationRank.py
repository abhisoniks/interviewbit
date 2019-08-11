# Given a string, find the rank of the string amongst its permutations sorted lexicographically.
# Assume that no characters are repeated
class Solution:
    def facto(self,l):
        if l<=1:
            return 1
        p=1
        while l!=1:
            p=p*l
            l-=1
        return p

    def findNonCommon(self,A,B):
        p=Diff(A-B)
        print(p)
        return 1

    def findRank(self, A):
        l=len(A)
        B=[c for c in A]
        c=[c for c in A]
        c.sort()
        rank=0
        for i in range(0,len(A)):
            p=c.index(B[i])
            f=self.facto(len(B)-1-i)
            q=B[:i]
            r=c[:p]
            t=self.findNonCommon(q,r)
            print(B[i], f, t, q,r)
