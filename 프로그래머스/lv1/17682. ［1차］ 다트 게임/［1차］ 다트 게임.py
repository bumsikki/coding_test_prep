def solution(dartResult):
    answer = 0
    darts = []
    options = []
    check_ten = ""
    for i, dart in enumerate(dartResult):
        if dart.isnumeric():   
            target = dart
            if check_ten.isnumeric():
                darts.pop()
                target = 10
            
            value = 0
            if dartResult[i+1] == "S":
                value = int(target) ** 1
            elif dartResult[i+1] == "D":
                value = int(target) ** 2
            else:
                value = int(target) ** 3
            darts.append(value)
            
        elif dart == "*" or dart == "#":
            temp = (len(darts), dart)
            options.append(temp)
        check_ten = dart
    for tuple_ in options:
        index = tuple_[0]
        option = tuple_[1]
        if option == "*":
            if index > 1:
                for i in range(index-2, index):
                    darts[i] *= 2
            else:
                darts[index-1] *= 2
        else:
            darts[index-1] *= -1         
    
    
    print(darts)
    print(options)
    
    for dart in darts:
        answer += dart
            
            
    
    return answer