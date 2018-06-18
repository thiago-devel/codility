def solution(A):
    n = len(A)
    L = [-1] + A
    count = 0
    pos = (n + 1) // 2
    candidate = L[pos]
    for i in range(1, n + 1):
        if (L[i] == candidate):
            count = count + 1
#    if (count > pos):
    if (2*count > n):
        return candidate
    return -1


A = [2, 2, 2, 2, 2, 3, 4, 4, 4, 6]
B = [1, 1, 1, 1, 50]
C = [2,2,4,5]
D = []
E = [1,2,3]
F = [1,1,3]
target = E
print('Case1')
print(solution(C))
print('Case2')
print(solution(E))
print('Case3')
print(solution(F))
