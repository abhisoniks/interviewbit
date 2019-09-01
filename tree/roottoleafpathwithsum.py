class Solution:
    def pathSum(self, A, B):
        mainRes=[]
        self.hasPath(A,B,[],0,mainRes)
        return mainRes

    def hasPath(self,A,B,path,sum_,mainRes):
        if A==None:
            return
        path.append(A.val)
        sum_+=A.val
        if sum_==B and A.left==None and A.right==None:
            mainRes.append(path)
        if A.left!=None:
            self.hasPath(A.left,B,path,sum_,mainRes)
        if A.right!=None:
            self.hasPath(A.right,B,path,sum_,mainRes)
