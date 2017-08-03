mixedList = ['pandas',31,'Sup',95.8,'Hello world!']
numList = [350, 711, 180, 360, 100]
stringList = ["Jesus", "Becky", "Albert", "Joe"]

def pickListType(lst):
    newString = ''
    total = 0

    for value in lst:
        if isinstance(value, int) or isinstance(value, float):  
    #isinstance(object, classinfo) in this case the class info is integer whole number and floating decimal number
            total += value
        elif isinstance(value, str):
            newString += value

    if newString and total:
        print "The array you entered is of mixed type"
        print "String:", newString
        print "Total:", total

    elif newString:
        print "The array you entered is of string type"
        print "String:",newString

    else:
        print "The array you entered is of number(float or int) type"
        print "Total:", total

print pickListType(mixedList)
print pickListType(numList)
print pickListType(stringList)