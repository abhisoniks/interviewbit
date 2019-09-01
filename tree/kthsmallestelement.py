# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    def kthsmallest(self, A, B):
        res=[]
        self.inOrder(A,res)
        return res[B-1]

    def inOrder(self,A,res):
        if A.left!=None:
            p=self.inOrder(A.left,res)
        res.append(A.val)
        if A.right!=None:
            q=self.inOrder(A.right,res)
        return res
