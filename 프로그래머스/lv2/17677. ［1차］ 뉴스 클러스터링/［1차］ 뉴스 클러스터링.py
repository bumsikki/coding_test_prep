def group_setup(A):
    result = []    
    for i in range(len(A)-1):
        if not A[i].isalpha() or not A[i+1].isalpha():
            continue
        else:
            result.append(A[i:i+2].lower())
    return result

def get_A_and_B(A, B):
    # assume len(A) <= len(B)
    answer = 0
    B_ = B.copy()
    for a in A:
        if a in B_:
            B_.remove(a)
            answer += 1        
    
    return answer
   
def solution(str1, str2):
    answer = 0
    # default case
   
    A = group_setup(str1)
    B = group_setup(str2)
    
    # print(A, B)
    if len(A) == 0 and len(B) == 0:
        return 65536
    A_and_B = 0
    
    if len(A) <= len(B):
        A_and_B = get_A_and_B(A, B)
    else:
        A_and_B = get_A_and_B(B, A)
    
    # print(A_and_B)
    answer = A_and_B / (len(A) + len(B) - A_and_B)
    
    
    
    # print(answer)
    
    return int(answer * 65536)