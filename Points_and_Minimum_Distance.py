testcases = int(input())
for test in range(testcases):
    size = int(input())
    user_input = input()
    
    numbers = [int(num) for num in user_input.split()]
    
    numbers.sort()
    
    distance = 0
    
    xList = numbers[:(size)]
    yList = numbers[-(size):]
    
    pointList = []
    for x in range(size):
        pointList.append([xList[x],yList[size -1 - x]])
        
    for i in range(1, size):
        bonus = abs(xList[i] - xList[i -1]) + abs(yList[i] - yList[i -1])
        distance += bonus
    print(distance)
    for (x,y) in pointList:
        print(f'{x} {y}')