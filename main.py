'''
Task 1:

1 - in example : simple and clear but no exceptions processing
2 - my realization: TypeError exception added
'''
def isEven(value: int) -> bool:
	try:
		return value%2==0
	except TypeError:
		print("TypeError: value must be int")
		return False

'''
Task 2:
(Python 2.7.18)

FIFO implementation
based on the list vs dict

pros & cons:

 - It's more efficient to use dict for the lookup of elements
   as it is faster than a list and takes less time.
 - Lists keep the order of the elements.
 - Dicts in Python require very little space to store the data elements.
'''

class FIFO:
	def __init__(self):
		self.data = []
	def put(self, elem):
		self.data.append(elem)
	def out(self):
		if len(self.data) > 0:
			del self.data[0]
	def _len(self):
		return len(self.data)

x = FIFO()
x.put(1)
print "answer" ,x;
print "len", x._len()
x.out()
print "len", x._len()


class FIFO_dict:
	def __init__(self):
		self.data = {}
		self.cur_back = 0
		self.cur_front = 0
	def put(self, elem):
		self.data[self.cur_back] = elem
		self.cur_back += 1
	def out(self):
		if len(self.data) > 0:
			del self.data[self.cur_front]
			self.cur_front += 1
	def _len(self):
		return len(self.data)


y = FIFO_dict()
y.put(1)
print "answer", y;
y.put(2)
y.put(3)
y.put(4)
y.put(5)
print "len", y._len()
y.out()
y.out()
print "len", y._len()

'''
Task 3:

The most well-known algorithm to sorting lists is qsort
but in the worst input we get a O(n^2)
so we will use a mergesort:
best & average & worst: O(nlogn)

Input:
3 2 1
Output:
1 2 3
'''


def merge(left, right):

    if len(left) == 0:
        return right
    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0
    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1
        if index_right == len(right):
            result += left[index_left:]
            break
        if index_left == len(left):
            result += right[index_right:]
            break

    return result

def merge_sort(array):
    if len(array) < 2:
        return array
    mid = len(array) // 2
    return merge(
        left=merge_sort(array[:mid]),
        right=merge_sort(array[mid:]))

list =[int(n) for n in input().split()]
print(*merge_sort(list))
