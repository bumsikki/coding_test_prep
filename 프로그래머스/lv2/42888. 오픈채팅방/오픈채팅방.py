def solution(record):
    answer = []
    dict_ = {}
    action_orders = []
    for rec in record:
        rec = rec.split(" ")
        action = rec[0]
        id_ = rec[1]
        
        
        temp = {
            "action" : "enter",
            "id" : id_
        }
        if action == "Change":  
            name = rec[2]
            dict_[id_] = name
        else:
            if action == "Enter":
                name = rec[2]
                dict_[id_] = name
            temp["action"] = action
            action_orders.append(temp)
    
    # print(action_orders)
    for order in action_orders:
        if order['action'] == "Enter":
            answer.append("{}님이 들어왔습니다.".format(dict_[order['id']]))
        else:
            answer.append("{}님이 나갔습니다.".format(dict_[order['id']]))
    return answer