# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def lca(self, A, B, C):
        if A.left==None and A.right==None:
            if A.val==B and A.val==C:
                return A.val
            else:
                return -1
        if B==C and A.val==B:
            return A.val
        flag=[False]
        p=self.findLca(A,B,C,flag)
        if flag[0]:
            return p.val
        return -1

    def findLca(self,A,B,C,flag):
        if A==None:
            return None
        a=self.findLca(A.left,B,C,flag)
        b=self.findLca(A.right,B,C,flag)
        if (A.val==B or A.val==C) and (a or b):
            flag[0]=True
            return A
        if A.val==B and B==C:
            flag[0]=True
            return A
        if A.val==B or A.val==C:
            return A
        if a and b:
            flag[0]=True
            return A
        if a:
            return a
        return b
        
