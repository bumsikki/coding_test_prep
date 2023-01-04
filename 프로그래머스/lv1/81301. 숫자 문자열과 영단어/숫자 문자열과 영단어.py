def solution(s):
    answer = ""
    
    dict_ = {}
    dict_["zero"] = "0"
    dict_["one"] = "1"
    dict_["two"] = "2"
    dict_["three"] = "3"
    dict_["four"] = "4"
    dict_["five"] = "5"
    dict_["six"] = "6"
    dict_["seven"] = "7"
    dict_["eight"] = "8"
    dict_["nine"] = "9"
    
    keys = list(dict_.keys())
    
    i = 0
    remember = False
    remember_index = 0
    while i < len(s):
        if s[i].isdigit():
            answer += s[i]
        else:
            target = ""
            if remember:
                target = s[remember_index: i+1]
            else:
                remember = True
                target = s[i]
                remember_index = i
            print(target)
            if target in keys:
                answer += dict_[target]
                remember = False
                
        i += 1
    print("answer:", answer)
    answer = int(answer)
    return answer