# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isSymmetric(self, A):
        return self.areChildSymmetric(A.left,A.right)
    def areChildSymmetric(self, A, B):
        if A==B:
            return 1
        if A==None or B==None:
            return 0
        if A.val!=B.val:
            return 0
        p=self.areChildSymmetric(A.left,B.right)
        q=self.areChildSymmetric(A.right,B.left)
        return p and q
