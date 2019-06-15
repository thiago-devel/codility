def oddOcurrencyInArray(A):
    result = set()
    
    for item in A:
        if (item in result):
            result.remove(item)
        else:
            result.add(item)
    
    return list(result)[0]

# TESTS

array = [42]
arrayExpected = 42
result = oddOcurrencyInArray(array)
print('In the provided array {' + str(array) + '} the odd item is {' + str(result) + '} and the expected was {' + str(arrayExpected) + '}')

array = []
last = 0
for i in range(0, (3)):
    array.insert(len(array), i)
    array.insert((len(array) + 1), i)
    last = i
array.insert(len(array), (last + 1))
arrayExpected = 3
result = oddOcurrencyInArray(array)
print('In the provided array {' + str(array) + '} the odd item is {' + str(result) + '} and the expected was {' + str(arrayExpected) + '}')

array = [9, 3, 9, 3, 9, 7, 9]
arrayExpected = 7
result = oddOcurrencyInArray(array)
print('In the provided array {' + str(array) + '} the odd item is {' + str(result) + '} and the expected was {' + str(arrayExpected) + '}')

array = [44, 3, 44, 3, 9, 102, 102]
arrayExpected = 9
result = oddOcurrencyInArray(array)
print('In the provided array {' + str(array) + '} the odd item is {' + str(result) + '} and the expected was {' + str(arrayExpected) + '}')
