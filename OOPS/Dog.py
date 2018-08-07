class Vehicle(object):

	type = "Car"

	def __init__(self,make,model):
		self.make = make
		self.model = model


	# def __init__(self):
	# 	self.make = make


class Sedan(Vehicle):
	def __init__(self):
		self.make = "Toyota"
		self.model = "Corolla"
	type = "Sedan"


ford = Vehicle("ford","f-150")
mustang = Vehicle("ford","mustang")

corolla = Sedan()
print("Make = " + corolla.make + " Model = " + corolla.model + " Type = " + corolla.type)


print("Make is " + ford.make + " and Model is " + ford.model + "Type = " + ford.type)
print("Make is " + mustang.make + " and Model is "+ mustang.model)
