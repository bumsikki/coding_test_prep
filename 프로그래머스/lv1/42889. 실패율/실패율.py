def solution(N, stages):
    answer = []
    stage_dict = {}
    cleared = []
    failure_rates = []
    for i in range(N+1):
        cleared.append(0)
    
    for stage in stages:
        if stage in stage_dict:           
            stage_dict[stage] += 1
        else:
            stage_dict[stage] = 1
        
        for j in range(stage):
            cleared[j] += 1
    
    for i, c in enumerate(cleared):
        failure_rate = 0
        if i+1 in stage_dict:
            failure_rate = stage_dict[i+1] / c
        failure_rates.append(failure_rate)
    
    failure_rates.pop()
    
    answer = list(reversed([N-i[0] for i in sorted(enumerate(reversed(failure_rates)), key=lambda x: x[1])]))
    
    # how to sort a list in a way that priorities the item that has higher value and lower index ?
    
    # print(cleared)
    # print(stage_dict)
    print(failure_rates)
    print(answer)
    
    return answer