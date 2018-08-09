import random

def oddOcurrencyInArray(A):
    result = -1
    
    if (len(A) == 0):
        return result
    
    if (len(A) == 1):
        return A[0]
    
    doNotRepeatedItens = set(A)

    separationMap = {}
    for item in A:
        if (len(doNotRepeatedItens) == 1):
            break
        if ((item in separationMap) and (item in doNotRepeatedItens)):
            doNotRepeatedItens.remove(item)
        separationMap[item] = item
    
    result = list(doNotRepeatedItens)[0]
    
    return result

# TESTS


def random_ints(num, lower=0, upper=9):
    return [random.randrange(lower, (upper + 1)) for i in range(num)]

array = [42]
arrayExpected = 42
result = oddOcurrencyInArray(array)
print 'In the provided array {' + str(array) + '} the odd item is {' + str(result) + '} and the expected was {' + str(arrayExpected) + '}'

array = []
last = 0
for i in range(0, (3)):
    array.insert(len(array), i)
    array.insert((len(array) + 1), i)
    last = i
array.insert(len(array), (last + 1))
arrayExpected = 3
result = oddOcurrencyInArray(array)
print 'In the provided array {' + str(array) + '} the odd item is {' + str(result) + '} and the expected was {' + str(arrayExpected) + '}'

array = [9, 3, 9, 3, 9, 7, 9]
arrayExpected = 7
result = oddOcurrencyInArray(array)
print 'In the provided array {' + str(array) + '} the odd item is {' + str(result) + '} and the expected was {' + str(arrayExpected) + '}'

array = [44, 3, 44, 3, 9, 102, 102]
arrayExpected = 9
result = oddOcurrencyInArray(array)
print 'In the provided array {' + str(array) + '} the odd item is {' + str(result) + '} and the expected was {' + str(arrayExpected) + '}'

array = random_ints(201, 0, 1000000000)
result = oddOcurrencyInArray(array)
print 'Odd item is {' + str(result) + '}'

array = random_ints(601, 0, 1000000000)
result = oddOcurrencyInArray(array)
print 'Odd item is {' + str(result) + '}'

'''
array = random_ints(2.001, 0, 1000000000)
arrayExpected = 2.001
result = oddOcurrencyInArray(array)

print 'Odd item is {' + str(result) + '} and the expected was {' + str(arrayExpected) + '}'
array = random_ints(100.003, 0, 1000000000)
arrayExpected = 100.003
result = oddOcurrencyInArray(array)
print 'Odd item is {' + str(result) + '} and the expected was {' + str(arrayExpected) + '}'
'''