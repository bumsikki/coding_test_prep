import math
def manh_dis(a,b):
    # a = [y1, x1]
    # b = [y2, x2]
    y_ = a[0] - b[0]
    x_ = a[1] - b[1]
    if y_ < 0:
        y_ *= -1
    if x_ <0:
        x_ *= -1
    return x_ + y_

def solution(numbers, hand):
    answer = []
    right_pos = [3, 2]
    left_pos = [3, 0]
    for num in numbers:  
        y = (num-1) // 3
        x = (num-1) % 3
        if num == 0:
            y = 3
            x = 1
        target = [y, x]
        print(num, target)
        if x == 0: 
            # Left Hand
            answer.append("L")
            left_pos = [y, x]
        elif x == 2:
            # Right Hand
            answer.append("R")
            right_pos = [y, x]
        else:
            # Choose a hand that is close to you 
            left_distance = manh_dis(target, left_pos)
            right_distance = manh_dis(target, right_pos)
            if left_distance > right_distance:
                # choose right hand
                answer.append("R")
                right_pos = [y, x]
            elif left_distance < right_distance:
                # choose left hand
                answer.append("L")
                left_pos = [y, x]
            else:
                answer.append(hand.upper()[0])
                if hand[0] == "r":
                    right_pos = [y, x]
                else:
                    left_pos = [y, x]
         
    return "".join(answer)