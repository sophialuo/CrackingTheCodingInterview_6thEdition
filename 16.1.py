'''
Number Swapper: Write a funciton to swap a number in place (that is, without temporary variables)
'''

def swap_numbers(arr, index0, index1):
	arr[index0], arr[index1] = arr[index1], arr[index0]

test = [1, 2, 3, 4]
swap_numbers(test, 1, 2)
print(test)