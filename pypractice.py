# Python3 code to demonstrate
# removing front element
# using deque() + popleft()
from collections import deque

# initializing list
test_list = [1, 4, 3, 6, 7]

# Printing original list
print("Original list is : " + str(test_list))

# using deque() + popleft() to
# perform removal
res = deque(test_list)
res.popleft()

# Printing modified list
print("Modified list is : " + str(list(res)))