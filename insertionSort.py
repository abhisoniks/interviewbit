# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def insertionSortList(self, A):
        if A==None or A.next==None:
            return A
        head=A
        current=A.next
        prev=A
        while current!=None:
            if current.val<prev.val:
                A=head
                A_prev=None
                temp=current.next
                while A.val<current.val:
                    A_prev=A
                    A=A.next
                if A_prev==None:
                    current.next=A
                    head=current
                    current=temp
                    prev.next=current
                    continue
                A_prev.next=current
                current.next=A
                current=temp
                prev.next=current
                continue
            prev=current
            current=current.next
        return head
