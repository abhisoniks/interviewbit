class Solution:
    def isBalanced(self, A):
        if self.getHeight(A)!=-1:
            return 1
        return 0
    def getHeight(self,root):
        if root==None:
            return 0
        a=self.getHeight(root.left)
        b=self.getHeight(root.right)
        if a==-1 or b== -1:
            return -1
        if abs(a-b) > 1:
            return -1
        return 1+max(a,b)
