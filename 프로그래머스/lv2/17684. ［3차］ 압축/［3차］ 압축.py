import string
def solution(msg):
    # 내 풀이 
    # 안됨 ㅠ 시간초과
#     answer = []
#     dict_ = {}
#     num = 1
    
#     for alphabet in string.ascii_uppercase:
#         dict_[alphabet] = num
#         num += 1
    
#     # num = 27
#     start = 0
#     end = 1
#     while start <= len(msg):
#         target = msg[start:end]
#         if target in dict_:
#             if end +1 > len(msg):
#                 answer.append(num)
#                 end += 1
#             else:
#                 end +=1
#         else:
#             answer.append(dict_[msg[start:end-1]])
#             dict_[target] = num
#             num += 1
#             start = end-1
#             #end = start + 1
    
#     answer.append(dict_[msg[start:end]])
    
    
    # 진혁이 풀이
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dics = []
    for j in alphabets:
        dics.append(j)
    
    start = 0
    end = 1
    answer = []
    while end <= len(msg):
        if msg[start:end] in dics:
            if end + 1 > len(msg):
                word = msg[start:end]
                o = dics.index(word)
                answer.append(o + 1)
                end += 1
            else :
                end += 1
            
            print("d",msg[start:end], start, end)
        else:
            word = msg[start:end-1]
            o = dics.index(word)
            answer.append(o + 1)
            dics.append(msg[start:end])
            print("a",msg[start:end], start, end)
            start = end - 1
        
    
    return answer