# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    def removeNthFromEnd(self, A, B):
        if A.next==None:
            if B>=1:
                return None
            return A
        head=A
        start=A
        faster=A
        count=0
        while count!=B:
            if faster==None:
                return head.next
            faster=faster.next
            count+=1
        if faster==None:
            return head.next
        while faster.next!=None:
            start=start.next
            faster=faster.next
        start.next=start.next.next
        return head
