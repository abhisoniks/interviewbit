# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    def partition(self, A, B):
        if A==None:
            return None
        head=None
        current=A
        if A.val<B:
            head=A
            current=A.next
        prev=A
        while current!=None:
            if current.val<B:
                if head==None:
                    head=current
                    temp=current.next
                    head.next=A
                    A=head
                    current=temp
                    prev.next=temp
                    continue
                elif current==A.next:
                    A=current
                    prev=current
                    current=current.next
                    continue
                else:
                    temp=current.next
                    current.next=A.next
                    A.next=current
                    A=current
                    prev.next=temp
                    current=temp
                    continue
            prev=current
            current=current.next
        if head!=None:
            return head
        return A
