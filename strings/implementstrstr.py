class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def strStr(self, A, B):
        lps=self.constructLPS(B)
        i=0
        j=0
        while i<len(A):
            while i<len(A) and j<len(B):
                if A[i]==B[j]:
                    i+=1
                    j+=1
                    continue
                else:
                    if j!=0:
                        j=lps[j-1]
                    else:
                        i+=1
            if j==len(B):
                return i-j
            else:
                return -1
        return -1


    def constructLPS(self,B):
        lps=[0]* len(B)
        i=1
        j=0
        while i <len(B):
            if B[i]==B[j]:
                lps[i]=lps[i-1]+1
                i+=1
                j+=1
                continue
            else:
                while j!=0:
                    j=lps[j-1]
                    if B[j]==B[i]:
                        lps[i]=lps[j]+1
                        break
                if j==0:
                    lps[i]=0
                i+=1
        return lps
