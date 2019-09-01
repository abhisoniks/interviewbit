# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal(self, A):
        stack=[]
        res=[]
        stack.append(A)
        while(stack):
            while(A!=None):
                if A.left!=None:
                    stack.append(A.left)
                A=A.left
            top=stack.pop()
            if top!=None:
                res.append(top.val)
                if top.right!=None:
                    stack.append(top.right)
                    A=top.right
        return res
