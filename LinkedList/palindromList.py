class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, A):
        if A.next==None:
            return 1
        middle=self.findMiddle(A)
        self.reverse(A,middle)
        p=A
        q=middle.next
        while q!=None:
            if p.val!=q.val:
                return 0
            p=p.next
            q=q.next
        return 1

    def findMiddle(self,A):
        single=A
        double=A.next
        while True:
            if double==None or double.next==None:
                return single
            double=double.next.next
            single=single.next


    def reverse(self,A,mid):
        head=mid
        head2=mid.next
        nextNode=mid.next
        temp=nextNode.next
        while temp!=None:
            nextNode.next=mid
            mid=nextNode
            nextNode=temp
            temp=temp.next
        nextNode.next=mid
        head2.next=None
        head.next=nextNode
        
