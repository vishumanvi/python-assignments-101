def invest(principal, rate, time):
	""" this function returns the investment amount """
	yearlyReturn = principal
	for n in range(1, time+1):
		yearlyReturn = yearlyReturn + (yearlyReturn*rate)/100
		print("Year %d: %6.2f" %(n, yearlyReturn))


invest(100, 5, 8)
