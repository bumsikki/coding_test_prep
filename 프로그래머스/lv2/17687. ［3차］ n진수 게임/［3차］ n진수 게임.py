def k_jinsu(n, k):
    result = []
    while n > 0:
        temp = divmod(n, k)
        assign = temp[1]
        if assign > 9:
            print(assign)
            ch = "A"
            assign = chr(ord(ch) + temp[1] - 10)
            result.append(assign)
        else:
            result.append(str(temp[1]))
        n = temp[0]
    return "".join(reversed(result))

def solution(n, t, m, p):
    answer = ''
    # n : 진법
    # m : 인원
    # p : 순서
    # t : 갯수
    
    cnt_num = 1
    game_record = "0"
    turn = 1
    whole_num = p + m * (t-1) 
    while len(game_record) < whole_num:
        game_record += k_jinsu(cnt_num, n)
        cnt_num += 1
    
    for i in range(t):
        target = i * m + p-1
        answer += game_record[target]
    
    print(game_record)
    
    
    return answer