def solution(lottos, win_nums):
    answer = []
    # default case
    
    num_zero = 0
    correct = 0
    for lotto in lottos:
        if lotto in win_nums:
            correct += 1
        elif lotto == 0:
            num_zero += 1
    
    print("n,z:", num_zero)
    print("cr:", correct)
    
    if correct == 6:
        return [1,1]
    if num_zero == 6:
        return [1, 6]
    
    
    # num_zero = 2
    # correct = 2
    # 최소 5등, 최고 3등
    best = 0
    worst = 0
    if correct < 2:
        worst = 6
        best = worst - num_zero + 1 - correct
        # best = worst - num_zero
        # if correct ==0:
        #     best += 1
    else:
        worst = 6 - correct + 1
        best = worst - num_zero
    
    answer = [best, worst]
        
    # 위는 내 풀이인데, 테스트 14번만 통과를 못함..
    
    # 아래는 참고한 풀이
    import math
    answer = [7 - max(correct+num_zero, 1), 7- max(correct, 1)]
    
    return answer