# Need to be fixed before submit
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

array = [44, 3, 44, 102, 9, 102, 9, 2]
arrayExpected = 3
result = oddOcurrencyInArray(array)
print 'In the provided array {' + str(array) + '} the odd item is {' + str(result) + '} and the expected was {' + str(arrayExpected) + '}'

array = [201]
arrayExpected = 201
result = oddOcurrencyInArray(array)
print 'In the provided array {' + str(array) + '} the odd item is {' + str(result) + '} and the expected was {' + str(arrayExpected) + '}'

array = [33, 33, 2.001, 8, 7, 7, 8]
arrayExpected = 2.001
result = oddOcurrencyInArray(array)
print 'In the provided array {' + str(array) + '} the odd item is {' + str(result) + '} and the expected was {' + str(arrayExpected) + '}'

