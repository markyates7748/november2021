## Weekend Exercise Work

# Define necessary functions
def calculate_bmi(weight, height):
    return weight / (height * height)

def get_weight_grade(bmi):
    if bmi >= 30:
        return 'obese'
    elif bmi >= 25:
        return 'over'
    elif bmi >= 18.5:
        return 'normal'
    else:
        return 'under'

def get_user_input(entries):
    enteredData = []
    for i in range(totalEntries):
        enteredData.append(input())
        enteredData[i] = enteredData[i].split(' ')
    return enteredData

# Take input
print('input data')
totalEntries = int(input())
enteredData = get_user_input(totalEntries)

# Work on input and print results
for i in enteredData:
    print(get_weight_grade(calculate_bmi(float(i[0]), float(i[1]))), end=' ')
print('')