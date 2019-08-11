# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        single=A
        double=A.next
        while double!=None and single!=double:
            single=single.next
            if double.next==None:
                double=double.next
                break
            double=double.next.next
        if double==None:
            return None
        c=A
        double=double.next
        while c!=double:
            c=c.next
            double=double.next
        return c
