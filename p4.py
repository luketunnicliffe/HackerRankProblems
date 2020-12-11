#!/usr/bin/env python3



# adds array numbers in a diagonal pattern

def diagonalDifference(arr):
	
	sum1 = 0
	sum2 = 0
	counter = len(arr)-1
	j = 0
	
	for i in range(len(arr)):
		print(arr[i][j])
		
		sum1 = arr[i][j] + sum1
		i += 1
		j += 1
		#print(sum1)
	
	for i in range(len(arr)):		
		sum2 = arr[i][counter] + sum2
		i += 1
		counter -= 1
	answer = abs(sum1-sum2)
	
	#print(sum1)
	#print(sum2)
	#print(answer)
	return answer
	
	
diagonalDifference(([11,2,4],[4,5,6],[10,8,-12]))
