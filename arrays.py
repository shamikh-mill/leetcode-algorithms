# With input an array of integers, reorder the entries so that even entries appear first. Do this without any additional space. 

def even_odd(A): 
	next_even, next_odd = 0, len(A) - 1
	while next_even < next_odd:
		if A[next_even] % 2 == 0: # if even, go to next 
			next_even += 1
		else: # if A[next_even] is odd, swap it to the front of the odd subsection
			A[next_even], A[next_odd] = A[next_odd], A[next_even] # pythonic list swap without dummy (must be one line)
			next_odd -= 1 # decrement start of odd subarray 
	return A 

print (even_odd([1,1,1,1,1,11,4,6,6,6]))


# partition the array into 3 subarrays- even, unclassified, and odd, in that order- even is at the beginning, and odd is at the end. 
# Initially even and odd are empty, unclassified is the entire array, and we interate through unclassified and keep the elements at the front if even or move to front of odd with swaps. 


# Swapping two values 
i = ['b', 'a']
a, b = i.index('a'), i.index('b')
i[b], i[a] = i[a], i[b]
# or i[a], i[b] = i[b], i[a] 
print (i)

# Reverse list: A[::-1]
A = [1, 2, 3, 4, 5]
print (A[2:] + A[:2])
print (A[1:2:3])