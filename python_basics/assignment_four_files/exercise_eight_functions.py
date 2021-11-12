## Part A
print('\nCoding Exercise 8\n')

#TODO: Part 1
print("1: func to print 'Hello World'")
def func():
    print('Hello World')
func()
print('')

#TODO: Part 2
print('2: func to print with input')
def func1(name):
    print('Hi My name is {}'.format(name))
func1('Mark')
print('')

#TODO: Part 3
print('3: func to print string 1 or 2 based on T/F input')
def func3(x, y, z):
    if z:
        return x
    else:
        return y
print(func3('hello', 'goodbye', False))
print(func3('hello', 'goodbye', True))
print('')

#TODO: Part 4
print('4: func to multiply input')
def func4(x, y):
    return x * y
print(func4(3,9))
print('')

#TODO: Part 5
print('5: func to test if input is even')
def is_even(testMe):
    if testMe % 2 == 0:
        return True
    else:
        return False
print(is_even(6))
print(is_even(5))
print('')

#TODO: Part 6
print('6: func that tests if number 1 is greater than number 2')
def compare(x, y):
    if x > y:
        return True
    else:
        return False
print(compare(2,1))
print(compare(1,2))
print('')

#TODO: Part 7
print('7: func that sums an arbitrary number of input')
def totalSum(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
print(totalSum(1,2,3,4))
print('')

#TODO: Part 8
print('8: func that returns list of even numbers from arbitrary number of input')
def evenNumbers(*args):
    tempList = []
    for i in args:
        if i % 2 == 0:
            tempList.append(i)
    return tempList
print(evenNumbers(1,2,3,4))
print('')

#TODO: Part 9
print('9: func that creates string of alternating case')
def alternatingCase(x):
    tempString = ''
    i = 1
    for ch in x:
        if i % 2 == 0:
            tempString = tempString + ch.upper()
        else:
            tempString = tempString + ch.lower()
        i += 1
    return tempString
print(alternatingCase('johnny'))
print('')

#TODO: Part 10
print('10: func that returns smaller number if both are even, greater if at least one is odd')
def func10(x, y):
    if x % 2 == 0 and y % 2 == 0:
        return x if x <= y else y
    else:
        return x if x >= y else y
print(func10(2,4))
print(func10(1,3))
print('')

#TODO: Part 11
print('11: func that tests if two strings start with the same letter')
def startWithSameLetter(x, y):
    if x[0] == y[0]:
        return True
    else:
        return False
print(startWithSameLetter('apple','avocado'))
print(startWithSameLetter('apple','banana'))
print('')

#TODO: Part 12
print('12: func that returns doubled distance from the other side of 7')
def doubledDistanceFrom7(x):
    if x < 7:
        distance = (7 - x) * 2
        return 7 + distance
    elif x > 7:
        distance = (x - 7) * 2
        return 7 - distance
    else:
        return 7
print(doubledDistanceFrom7(6))
print(doubledDistanceFrom7(7))
print(doubledDistanceFrom7(8))
print('')

#TODO: Part 13
print('13: func that capitalizes first and fourth characters of a string')
def capitalizeFirstAndFourth(x):
    tempString = ''
    tempString += x[0].upper()
    tempString += x[1:3]
    tempString += x[3].upper()
    tempString += x[4:]
    return tempString
print(capitalizeFirstAndFourth('johnny'))
print('')