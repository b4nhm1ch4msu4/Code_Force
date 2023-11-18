testcases = int(input())
for case in range(testcases):
    leng = int(input())
    
    # convert string to array
    array_input = input()
    numbersList = [int(num) for num in array_input.split()]
    
    temp_list = [numbersList[0]] * leng
    temp_list[0] = numbersList[0]
    
    for i in range(1,leng):
        if (numbersList[i] + numbersList[i-1]) % 2 == 0:
            temp_list[i] = numbersList[i]
        else:
            temp_list[i] = max((numbersList[i] + temp_list[i-1]),numbersList[i])
               
    _max = temp_list[0]
    for item in temp_list:
        if item > _max:
            _max = item
    print(_max)