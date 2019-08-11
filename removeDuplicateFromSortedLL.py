# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        head=A
        after=A.next
        while after!=None:
            while after !=None and after.val ==A.val:
                after=after.next
            A.next=after
            if after!=None:
                temp=after
                after=after.next
                A=temp
        return head
