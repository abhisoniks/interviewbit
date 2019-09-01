# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def preorderTraversal(self, A):
        res=[]
        stack=[]
        stack.append(A)
        res.append(A.val)
        while(stack):
            while(A!=None):
                if A.left!=None:
                    res.append(A.left.val)
                    stack.append(A.left)
                A=A.left
            top=stack.pop()
            if top!=None:
                if top.right!=None:
                    res.append(top.right.val)
                    stack.append(top.right)
                A=top.right
        return res
