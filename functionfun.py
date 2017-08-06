
# Odd/Even Function

def odd_even():
	print 'Executing the odd/even function'
	for number in range(2001): #For Loop will stop at 2000
		print 'Number is ',number,'.',
		if(number % 2 == 0):  # If number is divisible by 2 then it's even
			print "This is an even number."
		else:
			print "This is an odd number."
odd_even()

# Multiplication Function

def multiply(arr, num):
    for x in range(0, len(arr)):  #length of array
        arr[x] *= num
    return arr

numbersArray = [3, 6, 8, 10, 67]

print multiply(numbersArray, 5)

	
