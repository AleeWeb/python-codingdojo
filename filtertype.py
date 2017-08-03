
# Assignment Filter by Type


# Filter by Integer
def numbers():
	for i in range(151):
		if i >= 100:    
			print  i, "That's a big number!" #prints #100-150 with string
		elif i < 100:
			print i, "That's a small number."  #prints #0-#99

numbers()

# Filter String

def stringFilter():

	greeting = "Hey Becky. How are you? Bla Bla!"
	print len(greeting)

	latin = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc auctor est nec hendrerit consectetur. Sed interdum, risus nec hendrerit vulputate, nulla elit aliquam nisl, vel tincidunt magna ex ac lectus. Aliquam tempor lectus vel vehicula  consequat. Nullam accumsan felis et tellus luctus, in pretium nulla mattis. Sed elementum eget ex vel consectetur."
	print len(latin)

	if len(greeting) < 50:
		print "Short sentence."

	elif len(latin) >= 50:
		print "Long sentence."

stringFilter()


# Filter List

def filterList():
	sI = 45
	mI = 100
	bI = 455
	eI = 0
	spI = -23
	sS = "Rubber baby buggy bumpers"
	mS = "Experience is simply the name we give our mistakes"
	bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
	eS = ""
	aL = [1,7,4,21]
	mL = [3,5,7,34,3,2,113,65,8,89]
	lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
	eL = []
	spL = ['name','address','phone number','social security number']

	less10 = aL

	greater10 = lL

	if len(lL) >= 10:
		print "Big List!"

	elif len(less10) < 10:
		print "Short List"


filterList()
