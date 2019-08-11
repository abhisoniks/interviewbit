class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
        return self.calGcd(A,B)

    def calGcd(self,m,n):
        if n==0:
            return m
        return self.calGcd(n,m%n)
