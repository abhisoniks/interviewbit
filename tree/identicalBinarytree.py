# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    def isSameTree(self, A, B):
        return self.checkVal(A,B)

    def checkVal(self,A,B):
        if A==B:
            return 1
        if A==None or B==None:
            return 0
        if A.val!=B.val:
            return 0
        a=self.checkVal(A.left,B.left)
        b=self.checkVal(A.right,B.right)
        if a == 0 or b== 0:
            return 0
        return 1
