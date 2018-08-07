def enrollment_stats(enrollmentList):
	try:
		noOfEnrolledStudents = []
		annualTuituionFees = []
		totalEnrolledStudents = 0
		totalTutionFees = 0

		for i in range(0,len(enrollmentList)):
			noOfEnrolledStudents.append(enrollmentList[i][1])
			totalEnrolledStudents += enrollmentList[i][1]
			annualTuituionFees.append(enrollmentList[i][2])
			totalTutionFees += enrollmentList[i][2]

		print("Total students: ", totalEnrolledStudents)
		print("Total tuituion: ", totalTutionFees)
		meanValue = mean(noOfEnrolledStudents)
		medianValue = median(noOfEnrolledStudents)
		print("Student mean: ", meanValue)
		print("Student median: ", medianValue)
		meanValue = mean(annualTuituionFees)
		medianValue = median(annualTuituionFees)
		print("Tuition mean: ", meanValue)
		print("Tuition median: ", medianValue)
	except (Exception):
		print("Error occured in enrollment_stats")
		print(Exception.with_traceback())

def mean(inputList):
	try:
		sum = 0
		for i in inputList:
			sum += i

		return (sum/len(inputList))
	except(Exception):
		print("Error occured in mean")


def median(inputList):
	try:
		inputList.sort()
		if len(inputList) % 2 != 0:
			medianValue = inputList[(int(len(inputList)/2))]
		else:
			upperIndex = inputList[(int(len(inputList)/2))]
			lowerIndex = inputList[(int((len(inputList)/2))-1)]
			medianValue = (inputList[lowerIndex] + inputList[upperIndex])/2

		return (medianValue)
	except(Exception):
		print("Error occured in median")


universities = [
['California Institute of Technology', 2175, 37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]
]

enrollment_stats(universities)


