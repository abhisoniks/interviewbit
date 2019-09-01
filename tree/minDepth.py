# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def minDepth(self, A):
        if A.left==None and A.right==None:
            return 1
        res=[]
        self.calDepth(A,res,0)
        return min(res)

    def calDepth(self,A,res,count):
        if A==None:
            return
        if A.left==None and A.right==None:
            res.append(1+count)
        self.calDepth(A.left,res,count+1)
        self.calDepth(A.right,res,count+1)
