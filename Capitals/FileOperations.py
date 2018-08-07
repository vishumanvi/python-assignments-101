file1 = open("/Users/vishu/PycharmProjects/RealPython/vihaan.txt","r+")
fileLine = file1.readline()
while fileLine != "":
	print (fileLine)
	fileLine = "hahaha"
	file1.writelines(fileLine)
	fileLine = file1.readline()
file1.close()


