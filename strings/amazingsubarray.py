class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        l=len(A)
        count=0
        for i in range(0,l):
            if A[i] in ['a','i','e','o','u']:
                count+=l-i
        return count
