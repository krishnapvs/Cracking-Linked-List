# Implement an algorithm to delete a node in the middle of a singly linked list, given only access to that node.

class Node:
	def __init__(self, cargo=0, next=None):
		self.cargo=cargo
		self.next=next

	def __str__(self):
		return str(self.cargo)

def printList(head):
	while(head):
		print head
		head=head.next
# creating a linked list
n1=Node(10)
temp=n1
for i in range(21):
	temp.next=Node(i)
	temp=temp.next
del(temp)
k=int(raw_input("Enter the value for k: "))
current=n1
runner=n1
if current.cargo==k:
	n1=current.next
	del current
	print ("Value deleted")
else: 
	while(runner.next.cargo!=k):
		runner=runner.next
	runner.next=runner.next.next
printList (n1)

