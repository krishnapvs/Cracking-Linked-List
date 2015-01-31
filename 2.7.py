# Implement a function to check if a linked list is a palindrome

def palindrome(head):
# Function to check if linked list is a palindrome
	start=head
	l=[]
	while(head):
		l.append(head.cargo)
		head=head.next
	while start:
		if start.cargo!=l.pop():
			print 'not palindrome'
			return
		else:
			start=start.next
	print "Palindrome"

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

for i in range(10,-1,-1):
	runner.next=Node(i)
	runner=runner.next

printList(l1.next)

print 
palindrome(l1.next)
