class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        sum_=0
        l=len(A)
        for i,val in enumerate(A):
            sum_=sum_ + (ord('Z')-ord(val))*pow(26,l-1-i)
            print(sum_)
            
