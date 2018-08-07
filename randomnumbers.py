from random import randint

heads=0
tails=0

for i in range(1, 30000):
	if (randint(0,1) == 0):
		heads += 1
	else:
		tails += 1

print("Avg = ", float(heads/tails))
