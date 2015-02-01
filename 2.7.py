# Implement a function to check if a linked list is a palindrome
def palindromeusingStack(head):
# Function to check if the linked list is a palindrome
# Key challenges are to identify the size, if it is not avaliable then we run one pointer till the end other till half
	end=half=head
	while(end):
		end=end.next
		if(end==None):
			break
		end=end.next
		half=half.next
	print half, end

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

for i in range(9,-1,-1):
	runner.next=Node(i)
	runner=runner.next

printList(l1.next)

print 
palindromeusingStack(l1)