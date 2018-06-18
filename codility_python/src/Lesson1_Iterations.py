def binaryGap(N):
    
    binaryRepresentation = "{0:b}".format(N)
    print 'Binary representation of {' + str(N) + '} is {' + binaryRepresentation + '}'
    
    gapsPositions = []
    for i in range(len(binaryRepresentation), 0, -1):
        if (binaryRepresentation[i - 1] == '1'):
            gapsPositions.append(i - 1)
    print 'The Binary representation {' + binaryRepresentation + '} has {' + str(len(gapsPositions)) + '} gapsPosition at {' + str(gapsPositions) + '}'
    
    longestGap = 0
    for i in range(len(gapsPositions) - 1):
        x = (gapsPositions[i] - (gapsPositions[i + 1])) - 1
        longestGap = x if (x > longestGap) else longestGap
    
    return longestGap

bNumber = 1041
longestGap = binaryGap(bNumber)
print 'The largest gap for the number {' + str(bNumber) + '} is {' + str(longestGap) + '}'
