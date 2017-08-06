#assignment to print a cool checkerboard made of asterisks

checkerBoard = 8
num= 0
for num in range(8):  #There are 8 required rows of stars in this assignment
    if num % 2 == 0:  #if number is divisible by two then it is an even number
        print "* * * *"
    else:
        print " * * * *"
    num+=1
			