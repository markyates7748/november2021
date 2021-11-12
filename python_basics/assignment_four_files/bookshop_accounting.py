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
#print('Part 2: create list of 2-tuples with original configuration')
#print('Done in [(orderNumber, bookTitleAndAuthor), (pricePerItem, quantity)] format')
#partTwoList = list(map(lambda x: [(x[0], x[1]), (x[3], x[2])], originalOrder))
#print(partTwoList)
#print('')
print('Done in [(orderNumber, totalPrice), ...] format')
partTwoList = list(map(lambda x: (x[0], x[2] * x[3]), originalOrder))
print(partTwoList)
print('')

#TODO: Part 3
#Altered list -> now [order number, (article number, quantity, price), ... (article number, quantity, price)]
#return list of 2-tuples of (order number, total price)
sampleNewList = [1234, [1, 5, 10.99], [2, 6, 8.99], [3, 4, 12.95]]
print('Part 3: create a list of 2-tuples with new configuration')
finalTuple = (sampleNewList[0], sum(list(map(lambda x: x[1] * x[2], sampleNewList[1:]))))
print(finalTuple)