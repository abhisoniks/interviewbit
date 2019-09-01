class Solution:
    # @param A : string
    # @return string
    def reverseWords(self, A):
        a=A.split(" ")
        res=a[-1]
        for p in range(len(a)-2,-1,-1):
           res=" "+a[p]
        return res
