def drawStars():

	numList = [3, 26, 100, 3, 5, 7, 25]

	numList = input("List of integers and strings: ")
	for i in range(len(numList)):
		if(isinstance(numList[i],int)):
			print '*'* numList[i]
		else:
			print numList[i][0]*len(numList[i])

def drawStars(num):

	listX = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
	for item in num:

	