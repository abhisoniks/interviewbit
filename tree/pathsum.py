# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def hasPathSum(self, A, B):
        if self.findPath(A,B):
            return 1
        return 0
    def findPath(self,A,B):
        if A==None:
            return False
        if A.val==B and A.left==None and A.right==None:
            return True
        return self.findPath(A.left,B-A.val) or self.findPath(A.right,B-A.val)
