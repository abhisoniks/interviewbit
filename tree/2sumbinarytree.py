# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    def t2Sum(self, A, B):
        inorder=[A]
        reverse=[A]
        while inorder[-1].left!=None:
            inorder.append(inorder[-1].left)
        while reverse[-1].right!=None:
            reverse.append(reverse[-1].right)
        while inorder and reverse:
            if inorder[-1].val+reverse[-1].val<B:
                top=inorder.pop()
                if top.right!=None:
                    inorder.append(top.right)
                    while inorder[-1].left!=None:
                        inorder.append(inorder[-1].left)
            elif inorder[-1].val+reverse[-1].val>B:
                top=reverse.pop()
                if top.left!=None:
                    reverse.append(top.left)
                    while reverse[-1].right!=None:
                        reverse.append(reverse[-1].right)
            else:
                return 1
        return 0
