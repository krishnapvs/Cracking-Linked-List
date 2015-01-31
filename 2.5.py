#You have two numbers represented by a linked list, where each node contains a single digit. The
#digits are stored in reverse order, such that the Ts digit is at the head of the list. Write a
#function that adds the two numbers and returns the sum as a linked list

def addList(l1,l2,total):
	carry=0
	if(l1):
		if (l1.next):
			carry=addList(l1.next,l2.next,total.next)
		
		if l1.cargo+l2.cargo+carry>=10:
			total.cargo=(l1.cargo+l2.cargo+carry)%10
			return 1
		else:
			total.cargo=(l1.cargo+l2.cargo+carry)
			return 0
	else:
		return 0	

class Node():
	def __init__(self, cargo=0,next=None):
		self.cargo=cargo
		self.next=next

	def __str__(self):
		return str(self.cargo)

def printList(l):
	while(l):
		print l,
		l=l.next


l1=Node(1)
runner=l1
for i in range(0,10):
	runner.next=Node(i)
	runner=runner.next

l2=Node(1)
runner=l2
for i in range(9,-1,-1):
	runner.next=Node(i)
	runner=runner.next

total=Node(1)
runner=total
for i in range(9,-1,-1):
	runner.next=Node(0)
	runner=runner.next

l1=l1.next
l2=l2.next

total=total.next


carry=addList(l1,l2,total)
print " ",
printList(l1)
print
print " ",
printList(l2)
print
print carry,
printList(total)
print

