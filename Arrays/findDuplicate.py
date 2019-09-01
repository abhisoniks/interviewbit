class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        arr=[0 for i in A]
        for i in A:
            if arr[i]!=0:
                return i
            arr[i]=1
        return -1
