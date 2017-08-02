

# Multiples
'''Part I - Write code that prints all the odd numbers from 1 to 1000. 
Use the for loop and don't use a list to do this exercise.
'''

 #loop from 0 to 1000
def oddNumpicker():
	for i in range(1,1001):
		if i % 2 != 0: # Checks if remainder is divisible by 2, if not = to 0, the number is odd!
			print i 
oddNumpicker()


'''
Part II - Create another program that prints all the multiples of 5 
from 5 to 1,000,000.
'''
def chooseFive():
	for i in range(5,1000001):
		if i % 5 == 0:
			print i
chooseFive()

# Sum List
'''
Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]
'''
a = [1, 2, 5, 10, 255, 3]
b = sum(a)
print b



# Average List
'''
Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]
'''

a = [1, 2, 5, 10, 255, 3]
def avgList():



