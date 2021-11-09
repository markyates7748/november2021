#TODO: Part One
numberOne = 50
numberTwo = 50
print(numberOne + numberTwo)

numberOne = 100
numberTwo = 10
print(numberOne - numberTwo)

#TODO: Part Two
#print(30+*6)
print(6^6)
print(6**6)
print(6+6+6+6+6+6)

#TODO: Part Three
print("Hello World")
print("Hello World : 10")

#TODO: Part Four
print("input data:")
userInput = input().split(" ")
startingLoan = int(userInput.pop(0))
loanSize = startingLoan
interestRate = int(userInput.pop(0))
months = int(userInput.pop(0))
monthlyPayment = 0
i = 1
while(loanSize >= 0):
    loanSize = startingLoan
    i = 1
    monthlyPayment += 1
    while(i <= months):
        loanSize += loanSize * ((interestRate / 100) / 12)
        loanSize -= monthlyPayment
        i += 1
print("answer:")
print(monthlyPayment)
