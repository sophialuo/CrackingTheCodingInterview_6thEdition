'''
17.20 
Continuous Median: Numbers are randomly generated and passed to a method. Write a program to find and maintain the median value as new values are generated
'''
def continuous_median(nums):
	if len(nums) >= 1:
		print("median: " + str(nums[0]*1.0))
	if len(nums) >= 2:
		print("median: " + str(sum(nums)/2.0))


	if len(nums) > 2:
		#set up the heaps
		max_heap = [min(nums[0], nums[1])]
		min_heap = [max(nums[0], nums[1])]

		for i in range(2, len(nums)):
			#find the current effective median to compare against
			cur_median = 0
			if len(max_heap) == len(min_heap):
				cur_median = (max_heap[0]+min_heap[0])/2.0
			elif len(max_heap) > len(min_heap):
				cur_median = max_heap[0]
			else:
				cur_median = min_heap[0]
			#add to max_heap of elements smaller than effective median or
			#min_heap of elements larger than effective median
			elem = nums[i]
			if elem < cur_median:
				max_heap.append(elem)
				heapq._heapify_max(max_heap)
			else:
				min_heap.append(elem)
				heapq.heapify(min_heap)
			#adjust for diff in heap sizes
			if len(max_heap) > len(min_heap)+1:
				min_heap.append(max_heap.pop(0))
				heapq.heapify(min_heap)
			if len(min_heap) > len(max_heap)+1:
				max_heap.append(min_heap.pop(0))
				heapq._heapify_max(max_heap)
			#print the current median
			if len(max_heap) == len(min_heap):
				print("median: " + str((max_heap[0]+min_heap[0])/2.0))
			elif len(max_heap) > len(min_heap):
				print("median: " + str(max_heap[0]*1.0))
			else:
				print("median: " + str(min_heap[0]*1.0))

lst = [6, 4, 5, 3, 1, 9, 8, 10]
continuous_median(lst)

