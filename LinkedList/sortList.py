# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
	def sortList(self, A):
	    if A==None or A.next==None:
	        return A
	    slow=A
	    fast=A.next
	    while fast!=None and fast.next!=None:
	        slow=slow.next
	        fast=fast.next.next
	    secondHead=slow.next
	    slow.next=None
	    q=self.sortList(A)
	    p=self.sortList(secondHead)
	    res=self.mergeSort(p,q)
	    return res

	def mergeSort(self,list1,list2):
	 #   self.printS("list1",list1)
	 #   self.printS("list2",list2)
	    if list1==None and list2!=None:
	        return list2
	    if list2==None and list1!=None:
	        return list1


	    A=None
	    head=A
	    p=list1
	    q=list2
	    if p.val<q.val:
	        A=p
	        p=p.next
	    else:
	        A=q
	        q=q.next
	    head=A
	    while p!=None and q!=None:
	  #      print("pq",p.val," ",q.val)
	        if p.val<q.val:
	            A.next=p
	            A=p
	            p=p.next
	        else:
	            A.next=q
	            A=q
	            q=q.next
	    if p!=None:
	       A.next=p
	    if q!=None:
	       A.next=q
	   # self.printS("head",head)
	    return head

	def printS(self,msg,list1):
	    print(msg,end=" ")
	    while list1!=None:
	        print(list1.val,end=" ")
	        list1=list1.next
	    print()
