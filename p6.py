#!/usr/bin/env python3

def plusMinus(arr):
	length = len(arr)
	zeroCounter = 0
	positiveCounter = 0
	negativeCounter = 0
	for i in arr:
		if i == 0:
			zeroCounter += 1
		elif i > 0:
			positiveCounter += 1
		elif i < 0:
			negativeCounter += 1
	
	zeroCounter = zeroCounter/length
	positiveCounter = positiveCounter/length
	negativeCounter = negativeCounter/length

	print(positiveCounter)
	print(negativeCounter)
	print(zeroCounter)


plusMinus([-4,3,-9,0,4,1])
