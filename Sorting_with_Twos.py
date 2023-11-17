import math

def canSort(array,m):
    if m == 1:
        return True
    for x in range(2**(m-1),2**m -1):
        if array[x] > array[x+1]:
            return False
    return canSort(array,m-1)

testcases = int(input())
for case in range(testcases):
    leng = int(input())
    array_input = input()
    numbersList = [int(num) for num in array_input.split()]
    answer = 'YES'
    
    mMax = math.floor(math.sqrt(leng))
    if not canSort(numbersList,mMax):
        answer = 'NO'
    if leng > 2**mMax:
        for x in range(2**mMax,leng-1):
            if numbersList[x] > numbersList[x+1]:
                answer = "NO"
                

    
    print(answer)
    
