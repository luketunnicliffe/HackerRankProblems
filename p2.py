#!/usr/bin/env python3

#Compare the Triplets Problem - https://www.hackerrank.com/challenges/compare-the-triplets/problem
def compareTriplets(a, b):
	Alice = 0
	Bob = 0
	for i in range(0, 3):
		if a[i] > b[i]:
			Alice = Alice + 1
		if b[i] > a[i]:
			Bob = Bob + 1
	print(Alice, Bob)
	returnArray=[Alice,Bob]
	print(returnArray)
	return returnArray
		
	

compareTriplets([5,6,7], [3,6,10])
compareTriplets([17,29,30], [99,16,8])
