## Part B
print('\nCoding Exercise 4\n')
#TODO: Part 1
mixedList = [123, 'word', 3.21]
print(mixedList)

#TODO: Part 2
nestedList = [1, [1,2]]
print(nestedList[1][1])

#TODO: Part 3
lst = ['a', 'b', 'c']
print(lst[1:])

#TODO: Part 4
weekDict = {'sunday':0, 'monday':1, 'tuesday':2, 'wednesday': 3, 'thursday':4, 'friday':5, 'saturday':6}
print(weekDict)

#TODO: Part 5
D = {'k1':[1, 2, 3]}
# d[k1][1] will output two errors as the name 'd' is incorrect and 'k1' is entered as a variable name, not a value
# the following change is necessary to get the second entry of the value assigned to the desired key
print(D['k1'][1])

#TODO: Part 6
listToBecomeTuple = [1, [2, 3]]
tupleFromList = tuple(item for item in listToBecomeTuple)
print(tupleFromList)

#TODO: Part 7
S = 'Mississippi'
S = ''.join(set(S))
print(S)

#TODO: Part 8
S = S + 'X'
print(S)

#TODO: Part 9
print(set([1, 1, 2, 3]))

#TODO: Question 1
for x in range(1999, 3201):
    if(x % 7 == 0):
        if(x % 5 != 0):
            print(x, end=',')
print('\n')

#TODO: Question 2
def factorial(val):
    if val == 0 or val == 1:
        return 1
    return val * factorial(val - 1)
print('Enter a number to find its factorial')
val = int(input())
print(factorial(val))

#TODO: Question 3
def createDict(entries):
    tempDict = {}
    for x in range(1, entries+1):
        tempDict[x] = x * x
    return tempDict
print('Enter a number to create a dictionary:')
entries = int(input())
print(createDict(entries))

#TODO: Question 4
print('Enter a sequence of comma seperated numbers:')
inputNumbers = input()
inputAsList = inputNumbers.split(',')
inputAsTuple = tuple(inputAsList)
print(inputAsList)
print(inputAsTuple)

#TODO: Question 5
class SimplePythonClass:
    def _init_(self):
        self.classString = ''
    def getString(self):
        self.classString = input()
    def printString(self):
        print(self.classString.upper())
sampleClass = SimplePythonClass()
print('Enter a string for the simple class')
sampleClass.getString()
sampleClass.printString()