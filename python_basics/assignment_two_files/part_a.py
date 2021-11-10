## Part A
print('\nCoding Exercise 3\n')
#TODO: Part 1
print('Hello World'[0])

#TODO: Part 2
print('thinker'[2:5])

#TODO: Part 3
S = 'hello'
print(S[1])
S = 'Sammy'
print(S[2:])

#TODO: Part 4
S = 'Mississippi'
S = ''.join(set(S))
print(S)

#TODO: Part 5
print('input data: (test for palindrome)')
numberOfInputs = int(input())
stringInput = []
for x in range(numberOfInputs):
    stringInput.append(input())
for testString in stringInput:
    #remove non-characters
    tempString = ''.join(ch for ch in testString if ch.isalnum())
    #reverse and compare while ignoring case
    tempStringRev = tempString[::-1]
    if(tempString.lower() == tempStringRev.lower()):
        print('Y', end=' ')
    else:
        print('N', end=' ')
print('')