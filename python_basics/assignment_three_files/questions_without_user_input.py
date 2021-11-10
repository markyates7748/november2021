## Part A
print('\nCoding Exercise 7\n')

#TODO: Part 1
for i in range(1500-1, 2700+1):
    if i % 7 == 0 and i % 5 == 0:
        print(i, end=',')
print('\n')

#TODO: Part 4/5
for i in range(1,6):
    print('* ' * i)
for i in range(4, 0, -1):
    print('* ' * i)
print('')

#TODO: Part 7
sampleNumbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(f'original list: {sampleNumbers}')
evenCount = 0
oddCount = 0
for i in sampleNumbers:
    if i % 2 == 0:
        evenCount += 1
    else:
        oddCount += 1
print('Number of even numbers: %d'%evenCount)
print('Number of odd numbers: %d'%oddCount)
print('')

#TODO: Part 8
sampleList = [1452, 11.23, 1+2j, True, 'w3resource', (0,-1), [5,2], {"class":"V","section":"A"}]
print(f'original list: {sampleList}')
for item in sampleList:
    print(f'item {item} is of type {type(item)}')
print('')

#TODO: Part 9
for i in range(0,7):
    if i == 3 or i == 6:
        continue
    print(i, end=' ')
print('')