"""
Python syntactical sugar 
https://docs.python.org/3/tutorial/controlflow.html
Runtime of operations
https://wiki.python.org/moin/TimeComplexity
"""
# Arrays 

A = list(range(10))
print ('reversal', A[::-1])
print (A[::2])


# Slicing A[i:j:k], k is step size


"""
With input an array of integers, reorder the entries so that the even entries appear first 
Solve without using additional space. 


"""


def even_odd(A: list):
	# divide the list into even part, unclassified part, odd part 
	# if we come to a number that is odd, swap with end 
	# move the increments by one 
	next_even, next_odd = 0, len(A) - 1
	while next_even < next_odd: 
		if A[next_even] % 2 == 0: 
			next_even += 1
		else: 
			A[next_even], A[next_odd] = A[next_odd], A[next_even]
			next_odd -= 1
	return A

print (even_odd([1, 2, 3, 4]))



"""
Dutch flag partition problem
All elements less than A[i] first, then equal to A[i], then greater than A[i]
"""
# O(n) additional space is trivial solution
def easy_dutch_flag_partition(A: list, pivot_index: int):
	return [x for x in A if x < A[pivot_index]] + [x for x in A if x == A[pivot_index]] + [x for x in A if x > A[pivot_index]]

print (easy_dutch_flag_partition([0, 1, 2, 0, 2, 1, 1], 3))


# No additional space 
def dutch_flag_partition(A: list, pivot_index: int):
	# divide array into less than, equal, and greater than subarrays.
	next_less, next_greater = 0, len(A) - 1
	pass 

print (dutch_flag_partition([0, 1, 2, 0, 2, 1, 1], 3))






# Stacks 
"""
Two main operations: Push and Pop
Push: append element to the top of the stack
Pop: Remove an element from the top of the stack

Only operate with data on one side of the stack
Useful for anything related to tracing back to last element/operation used 
- back in browser, brackets in code, undo operations
- keep track of valid recursions in code- each call to recursive function is 
stored to the stack to be executed once lower recursions execute 


Using lists as stacks 
Last element added is the first element removed (Last In First Out)
"""
stack = [3, 4, 5]

# add element to the top of the stack
stack.append(6)
print (stack)

# Return most recently added element, remove it from the top of the stack (pop)
# No index needed 
last_added = stack.pop()
print (last_added)
print (stack)

y = stack.pop()
print (y)
print (stack)


# More in-depth Python class Stack 
class Stack: 
	def __init__(self): 
		self.stack = []
	def pop(self): 
		if self.is_empty(): return None
		else: return self.stack.pop()
	def push(self, val): 
		return self.stack.append(val)
	def peek(self): 
		if self.is_empty(): return None
		else: return self.stack[-1]
	def size(self): 
		return len(self.stack)
	def is_empty(self): 
		return self.size() == 0


# Queues 

"""
Using lists as queues 
First element added is the first element removed (First In First Out)

Two main operations: Dequeue and enqueue 
Enqueue = append an element to the end of the queue (line)
Dequeue = Remove an element from the beginning of the queue (line)

Queues are useful when wanting to process things once at a time, 
uploading images, printing, processing requests 
"""
# Faster pythonic implementation
from collections import deque 
queue = deque(["A", "B", "C"])
arrive = queue.append("D")
leave = queue.popleft() # First one leaves
print (leave)
print (queue) # prints in order of arrival


# Class implementation- remember to deal with data at the front and the end 
# Don't mix up which is enqueue and which is dequeue 
class Queue: 
	def __init__(self): 
		self.queue = []
	def enqueue(self, item): # insert element at the start of the list 
		self.queue.insert(0, item)
	def dequeue(self): # Take element off of the end 
		if self.is_empty(): return None
		else: return self.queue.pop()
	def size(self): 
		return len(self.queue)
	def is_empty(self):
		return self.size() == 0

q = Queue()
q.enqueue(1)
print (q.dequeue())
print (q.is_empty())


# Non obvious list operations 
a = [2, 3]

# insert method 
a.insert(0, 1)
# inserts 1 at index 0 
# extend method 
a.extend([4, 4])
print (a)

a.index(1)
# Returns index of the first occurence of 1 in the list


# remove a specified element 
a.remove(1)
# removes the first 1 (element, not object, from list- error if no such element)

a.pop(2)
# Removes 2nd index element from the list, with no argument, removes last element. Also returns it 

a.count(1) 
# Return number of times 1 appears in the list 

a.reverse()
# in-place reversing of list 

a.sort()
# Sort list in place 

d = {'t': 1, 'r': 2, 'e': 3}
# sort dictionary by value
print (sorted(d.items(), key=lambda x:x[1], reverse = True))

# iterate through sorted list of tuples 
for x, y in sorted(d.items(), key=lambda x:x[1], reverse = True): 
	pass 
	# something with x and y 

"""

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""

def isValid(s: str): 
	stack = []
	map = {')':'(', '}':'{', ']':'['}
	for x in s: 
		if x in map.values(): 
			stack.append(x)
		else: 
			# if closing bracket, last bracket in stack must be opening bracket
			if map[x] != stack.pop():
				return False	
	# stack must be empty 
	return len(stack) == 0

print (isValid("([]"))
print (isValid("()[]{}"))


"""
Runtime 
How does the runtime increase with increase in size of input -> rate of growth of time taken with respect to the input 

When time taken does not depend on the input = constant time algorithm
"""


