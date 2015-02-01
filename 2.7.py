# Implement a function to check if a linked list is a palindrome
def palindromeusingStack(head):
# Function to check if the linked list is a palindrome
# Key challenges are to identify the size, if it is not avaliable then we run one pointer till the end other till half
	end=half=head
	counter = 0
	stack=[]
	while(end):
		end=end.next
		counter+=1
		if(end==None):
			break
		stack.append(half.cargo)
		end=end.next
		half=half.next
		counter+=1
	if(counter%2):
		half=half.next
	while(half):
		if (int(half.cargo)!=int(stack.pop())):
			print "Not a palindrome"
			return
		half=half.next
	print "Is a palindrome"
		


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

for i in range(0,15):
	runner.next=Node(i)
	runner=runner.next

for i in range(11,-1,-1):
	runner.next=Node(i)
	runner=runner.next
l1=l1.next
#printList(l1)

print 
palindromeusingStack(l1)