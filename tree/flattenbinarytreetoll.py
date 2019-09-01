# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def flatten(self, A):
        if A==None:
            return
        self.flatten(A.left)
        self.flatten(A.right)
        if A.left==None and A.right==None:
            return A
        if A.left==None:
            return
        temp=A.right
        A.right=A.left
        A.left=None
        if A.right!=None:
            B=A.right
            while B.right!=None:
                B=B.right
            B.right=temp
        return A
