from math import *

def is_prime(n):
    if(n > 1):
        for i in range(2, int(sqrt(n)) + 1):
            if (n % i == 0):
                return False
        return True
    return False
    
def k_jinsu(n, k):
    result = []
    while n > 0:
        temp = divmod(n, k)
        result.append(str(temp[1]))
        n = temp[0]
    return "".join(reversed(result))
    
    
def solution(n, k):
    answer = 0
    target = k_jinsu(n,k)
    print(target)
    target_list = target.split("0")
    print(target_list)
    record = []
    
    for x in target_list:
        if len(x) > 0:
            if is_prime(int(x)):
                answer += 1
                record.append(x)
    return answer