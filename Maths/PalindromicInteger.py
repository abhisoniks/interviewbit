#Determine whether an integer is a palindrome. Do this without extra space.

#A palindrome integer is an integer x for which reverse(x) = x where reverse(x) is x with its digit reversed.
#Negative numbers are not palindromic.

class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, A):
        l=len(str(A))
        while(l>1):
            p=int(A/pow(10,l-1))
            q=A%10
            if p!=q:
                return 0
            A=A%pow(10,l-1)
            A=A/10
            newL= len(str(A))
            while A!=0 and newL!=l-2:
                if A%10!=0:
                    return 0
                A=A/10
                newL+=1
            l=len(str(A))
        return 1
