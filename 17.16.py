'''
17.16 
The Masseuse. A popular masseuse receives a sequence of back-to-back appointment requests and is debating which ones to 
accept. She needs a 15 minute break between appointments and therefore she cannot accept any adjacent requests. Given
a sequence of back-to-back appointment requests (all multiples of 15 minutes, none over laps, and none can be moved),
find the optimal (highest total booked minutes) set the masseuse can honor. Return the number of minutes. 
EXAMPLE
Input: {30, 15, 60, 75, 45, 15, 15, 45}
Output: 180 minutes ({30, 60, 45, 45})
'''

def the_masseuse(times):
	oneWay, twoWay = 0, 0
	for i in range(len(times)-1, -1, -1):
		bestWith = times[i] + twoWay
		bestWithout = oneWay

		twoWay = oneWay
		oneWay = max(bestWith, bestWithout)

	return oneWay

times = [30, 15, 60, 75, 45, 15, 15, 45]
print(the_masseuse(times))