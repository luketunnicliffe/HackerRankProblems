#!/usr/bin/env python3


def simpleArraySum(ar):
	sum = 0
	for i in range(0, len(ar)):
		sum = sum + ar[i]
	print(sum)
	return sum
print(simpleArraySum([1,2]))


