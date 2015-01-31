# Implement an algorithm to find the kth to last element of a singly linked list.

class Node:
	def __init__(self, cargo=0, next=None):
	# initializes the node
		self.cargo=cargo
		self.next=next

	def __str__(self):
	# prints a node with value cargo
		return str(self.cargo)

def printList(head):
# prints the entire list
	while(head):
		print head
		head=head.next

n1=Node(3)
n=n1
# Building a vague list
for i in range(20):
	n.next=Node(i)
	n=n.next

runner=n1
current=n1
# Reads a value for k
k=int(raw_input("Enter value for k: "))
for i in range(k):
	runner=runner.next
while (runner.next):
	runner=runner.next
	current=current.next

print current
print


	
