from random import randint

trials = 10000
flips = 0

for i in range(0,10):
	firstFlip = randint(0,1)
	flips +=1
	while randint(0,1) == firstFlip:
		flips += 1
	flips += 1
print("total flips = ", flips)
print ("flips/trials", float(flips/trials))
