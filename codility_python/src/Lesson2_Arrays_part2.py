def oddOcurrencyInArray(A):
    result = 0
    
    for item in A:
        ocurrency = 0
        for j in A:
            if (ocurrency > 1):
                break
            
            if (j == item):
                ocurrency = ocurrency + 1
        
        
        if ocurrency < 2:
            result = item
            break
    
    return result


array = [9, 3, 9, 3, 9, 7, 9]
arrayExpected = 7
result = oddOcurrencyInArray(array)
print 'In the provided array {' + str(array) + '} the odd item is {' + str(result) + '} and the expected was {' + str(arrayExpected) + '}'

array = [44, 3, 44, 3, 9, 102, 102]
arrayExpected = 9
result = oddOcurrencyInArray(array)
print 'In the provided array {' + str(array) + '} the odd item is {' + str(result) + '} and the expected was {' + str(arrayExpected) + '}'

array = []
i = 0
while (i < 200):
    next = i + 1
    array.insert(i, i)
    if (i < 200):
        array.insert(next, i)
    i = next
arrayExpected = 201
result = oddOcurrencyInArray(array)
print 'In the provided array {' + str(array) + '} the odd item is {' + str(result) + '} and the expected was {' + str(arrayExpected) + '}'
'''
array = [33, 33, 2.001, 8, 7, 7, 8]
arrayExpected = 2.001
result = oddOcurrencyInArray(array)
print 'In the provided array {' + str(array) + '} the odd item is {' + str(result) + '} and the expected was {' + str(arrayExpected) + '}'
'''
