# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        if A==None:
            return B
        if B==None:
            return A
        head,p,q,loc=None,A,B,None
        if A.val<B.val:
            head=A
            loc=A
            p=A.next
        else:
            head=B
            loc=B
            q=B.next
        while not p and not q:
            print(head.val,p.val,q.val,loc.val)
            if p.val<q.val:
                loc.next=p
                loc=p
                p=p.next
            else:
                loc.next=q
                loc=q
                q=q.next
        if not p:
            loc.next=p
        if not q:
            loc.next=q
        return head
