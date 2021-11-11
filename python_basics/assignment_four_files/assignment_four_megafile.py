## Part A
print('\nCoding Exercise 8\n')

#TODO: Part 1
def func():
    print('Hello World')
func()
print('')

#TODO: Part 2
def func1(name):
    print('Hi My name is {}'.format(name))
func1('Mark')
print('')

#TODO: Part 3
def func3(x, y, z):
    if z:
        return x
    else:
        return y
print(func3('hello', 'goodbye', False))
print(func3('hello', 'goodbye', True))
print('')
#TODO: Part 4
def func4(x, y):
    return x * y
print(func4(3,9))
print('')

#TODO: Part 5
def is_even(testMe):
    if testMe % 2 == 0:
        return True
    else:
        return False
print(is_even(6))
print(is_even(5))
print('')

#TODO: Part 6
def compare(x, y):
    if x > y:
        return True
    else:
        return False
print(compare(2,1))
print(compare(1,2))
print('')

#TODO: Part 7
def totalSum(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
print(totalSum(1,2,3,4))
print('')

#TODO: Part 8
def evenNumbers(*args):
    tempList = []
    for i in args:
        if i % 2 == 0:
            tempList.append(i)
    return tempList
print(evenNumbers(1,2,3,4))
print('')

#TODO: Part 9
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
def func10(x, y):
    if x % 2 == 0 and y % 2 == 0:
        return x if x <= y else y
    else:
        return x if x >= y else y
print(func10(2,4))
print(func10(1,3))
print('')

#TODO: Part 11
def startWithSameLetter(x, y):
    if x[0] == y[0]:
        return True
    else:
        return False
print(startWithSameLetter('apple','avocado'))
print(startWithSameLetter('apple','banana'))
print('')

#TODO: Part 12
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
def capitalizeFirstAndFourth(x):
    tempString = ''
    tempString += x[0].upper()
    tempString += x[1:3]
    tempString += x[3].upper()
    tempString += x[4:]
    return tempString
print(capitalizeFirstAndFourth('johnny'))
print('')

## Part B
print('\nCoding Exercise 9\n')

#TODO: Part 1
# Order Number || Book Title and Author || Quantity || Price per Item
# 34587 || Learning Python, Mark Lutz || 4 || 40.95
# 98762 || Programming Python, Mark Lurz || 5 || 56.80
# 77226 || Head First Python, Paul Barry || 3 || 32.95
# 88112 || Einfuhrung in Python3, Bernd Klein || 3 || 24.99
originalOrder = [[34587, 'Learning Python, Mark Lutz', 4, 40.95],
                [98762, 'Programming Python, Mark Lurz', 5, 56.80], 
                [77226, 'Head First Python, Paul Barry', 3, 32.95], 
                [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]]

#TODO: Part 2
#return list with 2-tuples of (order number, product) and (price, quantity)
print('Part 2: create list of 2-tuples with original configuration')
partTwoList = list(map(lambda x: [(x[0], x[1]), (x[3], x[2])], originalOrder))
for i in partTwoList:
    print(i)
print('')

#TODO: Part 3
#Altered list -> now [order number, (article number, quantity, price), ... (article number, quantity, price)]
#return list of 2-tuples of (order number, total price)
sampleNewList = [1234, [1, 5, 10.99], [2, 6, 8.99], [3, 4, 12.95]]
print('Part 3: create a list of 2-tuples with new configuration')
finalTuple = (sampleNewList[0], sum(list(map(lambda x: x[1] * x[2], sampleNewList[1:]))))
print(finalTuple)
