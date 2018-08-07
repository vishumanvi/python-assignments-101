n = 100
cats = dict()
for i in range(100):
	cats[i] = False

print(cats)
for i in range(1, 101):
	for k in range(0, 100, i):
		if cats[k] == True:
			cats[k] = False
		else:
			cats[k] = True

for l in range(0,100):
	if cats[l] == True:
		print("cats[" + str(l) + "] is wearing a hat.")
		