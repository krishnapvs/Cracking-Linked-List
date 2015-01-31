# Given a circular linked list, implement an algorithm which returns the node at the beginning of the loop

def circularNode(head):
	#retuns the node at the begining of the loop
	fast_runner=head
	slow_runner=head
	fast_runner=fast_runner.next.next
	slow_runner=slow_runner.next
	while (fast_runner!=slow_runner):
		fast_runner=fast_runner.next.next
		slow_runner=slow_runner.next
	fast_runner=head
	while(fast_runner!= slow_runner):
		fast_runner=fast_runner.next
		slow_runner=slow_runner.next

	return fast_runner

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

printList(l1)

print 
runner.next=l1.next.next.next.next
print circularNode(l1)