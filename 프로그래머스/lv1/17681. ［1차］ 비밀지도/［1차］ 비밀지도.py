def color_decrypt(n, i, arr, decrypt):
    target = int(arr[i])
    cnt = 0
    while target > 0 :
            temp = divmod(target, 2) # (몫, 나머지)
            decrypt[cnt] = temp[1]
            target = temp[0]
            cnt+=1
            
    decrypt = list(reversed(decrypt))
    return decrypt
    
def solution(n, arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        decrypt = []
        for j in range(n):
            decrypt.append(0)
            
        decrypt1 = color_decrypt(n, i, arr1, decrypt)
        print(decrypt1)
        decrypt2 = color_decrypt(n, i, arr2, decrypt)
        print(decrypt2)
        
        answer_item = ""
        for x in range(n):
            if decrypt1[x] == 1 or decrypt2[x] == 1:
                answer_item += "#"
            else:
                answer_item += " "
        answer.append(answer_item)
        
       
        
        
    return answer