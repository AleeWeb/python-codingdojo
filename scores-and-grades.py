
'''
Write a function that generates ten scores between 60 and 100. Each time a score is generated, 
your function should display what the grade is for a particular score. Here is the grade table:

'''

def gradeScale():

	for i in range(60,101):  #Run the For Loop from numbers 60 to 100
	
		if i <= 70: 
			print "Score:", i,"; Your grade is D"

		elif i <= 80: 
			print "Score:", i,"; Your grade is C"

		elif i <= 90: 
			print "Score:", i,"; Your grade is B"


		elif i <= 100: 
			print "Score:", i,"; Your grade is A"
			

gradeScale()