# Given a positive integer which fits in a 32 bit signed integer,
# find if it can be expressed as A^P where P > 1 and A > 0. A and P both should be integers.

class Solution:
    # @param A : integer
    # @return an integer
    def isPower(self, A):
        if A==1:
            return 1
        p=math.log(A)
        l=int(math.sqrt(A))
        for i in range(2,l+1):
            q=math.log(i)
            x=p/q
            if pow(i,x)==A:
                print(i, "" ,x, "",A,"",pow(i,x))
                return 1
        return 0
