def arrayPositionsShit(A, K):
    
    result = []
    if (len(A) == int(K)):
        return A
    
    for i, item in enumerate(A):
        if i < K:
            result.insert((K + i), item)
        else:
            result.insert((i - K), item)
    
    return result

array = [1, 2, 3, 4]
arrayExpected = [3, 4, 1, 2]
shift = 2
result = arrayPositionsShit(array, shift)
print 'The provided array {' + str(array) + '} shifted in {' + str(shift) + '} new array positions are {' + str(result) + '} and the expected was {' + str(arrayExpected) + '}'

array = [1, 2, 3, 4, 5, 6]
arrayExpected = [6, 1, 2, 3, 4, 5]
shift = 5
result = arrayPositionsShit(array, shift)
print 'The provided array {' + str(array) + '} shifted in {' + str(shift) + '} new array positions are {' + str(result) + '} and the expected was {' + str(arrayExpected) + '}'

array = [0, 0, 0]
arrayExpected = [0, 0, 0]
shift = 3
result = arrayPositionsShit(array, shift)
print 'The provided array {' + str(array) + '} shifted in {' + str(shift) + '} new array positions are {' + str(result) + '} and the expected was {' + str(arrayExpected) + '}'

array = [3, 8, 9, 7, 6]
arrayExpected = [9, 7, 6, 3, 8]
shift = 3
result = arrayPositionsShit(array, shift)
print 'The provided array {' + str(array) + '} shifted in {' + str(shift) + '} new array positions are {' + str(result) + '} and the expected was {' + str(arrayExpected) + '}'


