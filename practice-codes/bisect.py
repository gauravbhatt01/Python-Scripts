'''


'''

import bisect
import random

def find_closet(numbers, my_val):
	i = bisect.bisect_left(numbers, my_val)
	j = 0

	if i == len(numbers):
		return i - 1	#zero indexing
	elif numbers[i] == my_val:
		return i
	elif i < 0:
		j = i - 1
		if numbers[i] - my_val > my_val- numbers[j]:
			return j
	return i

numbers = []
for i in xrange(10):
	new_number = random.randint(0,1000)
	bisect.insort(numbers, new_number)

closest_index = find_closet(numbers, 500)
print(numbers[closest_index])