def solution(s):
    answer = []
    
    answer_helper = {}
    # data 전처리
    s = s[1:-1].split("},")
    for i, item in enumerate(s):
        if i == len(s)-1:
            item = item[1:-1]
        else:
            item = item[1:]
        item = item.split(",")
        # print(item)
        # sort item in ascending order in terms of the size of the tuple
        
        answer_helper[len(item)] = item
    
    for i in range(1, len(answer_helper)+1):
        item = answer_helper[i]
        for target in item:
            if int(target) not in answer:
                answer.append(int(target))
    
    return answer