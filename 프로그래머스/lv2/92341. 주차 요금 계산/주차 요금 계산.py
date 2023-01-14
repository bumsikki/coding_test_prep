import math

def solution(fees, records):
    answer = []
    curr_parked = {} # 차량번호 : 입장시간
    total_parked = {} # 차량번호 : 누적주차시간
    
    min_time = fees[0]
    min_fee = fees[1]
    unit_time = fees[2]
    unit_fee = fees[3]
    
    for record in records:
        record = record.split(" ")
        car = record[1]
        temp = record[0].split(":")
        time = int(temp[0]) * 60 + int(temp[1])
        if record[2] == "IN":
            curr_parked[car] = time
        else:
            time_spent = time - curr_parked[car]
            if car in total_parked:
                total_parked[car] += time_spent
            else:
                total_parked[car] = time_spent
            curr_parked.pop(car)
    
    print(curr_parked)
    
    for stayed_car in curr_parked:
        time_spent = 24 * 60 - curr_parked[stayed_car] -1
        if stayed_car in total_parked:
            total_parked[stayed_car] += time_spent
        else:
            total_parked[stayed_car] = time_spent
            
    print(total_parked)        
    keys = list(sorted(total_parked.keys()))
    for key in keys:
        parking_fee = min_fee
        total_time = total_parked[key]
        if total_time > min_time:
            temp = total_time - min_time
            temp /= unit_time
            temp = math.ceil(temp)
            temp *= unit_fee
            parking_fee += temp
        answer.append(parking_fee)
    
    
    return answer