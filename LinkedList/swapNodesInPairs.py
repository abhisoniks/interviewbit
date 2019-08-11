# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):
        if A==None or A.next==None:
            return A
        prev=None
        first=A
        second=A.next
        ref=second
        if second.next==None:
            second.next=A
            A.next=None
            return second
        third=second.next
        while third!=None:
            second.next=first
            if prev==None:
                prev=first
            else:
                prev.next=second
                prev=first
            first=third
            second=third.next
            if third.next!=None:
                third=third.next.next
            else:
                prev.next=third
                break
        if first!=None and second!=None:
            second.next=first
            prev.next=second
            first.next=None
        return ref
