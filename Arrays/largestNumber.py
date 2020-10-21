from functools import cmp_to_key
class Solution:
    def largestNumber(self, A):
        A= [ str(i) for i in A]
        A = "".join(sorted(A, key= mySort))
        print(A)
        return "0" if A.lstrip("0")=="" else A

def mySort(a,b):
    return 1 if  a+b > b+a else return -1
