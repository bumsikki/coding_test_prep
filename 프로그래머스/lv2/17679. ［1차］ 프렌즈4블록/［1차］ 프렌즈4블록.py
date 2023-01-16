def check_SE(board, x, y):
    target = board[y][x] 
    if board[y][x+1] != target:
        return False
    if board[y+1][x+1] != target:
        return False
    if board[y+1][x] != target:
        return False
    return True

def check_SW(board, x, y):
    target = board[y][x]
    if board[y][x-1] != target:
        return False
    if board[y+1][x] != target:
        return False
    if board[y+1][x-1] != target:
        return False
    return True

def check_NW(board, x, y):
    target = board[y][x]
    if board[y-1][x] != target:
        return False
    if board[y-1][x-1] != target:
        return False
    if board[y][x-1] != target:
        return False
    return True

def check_NE(board, x, y):
    target = board[y][x]
    if board[y-1][x] != target:
        return False
    if board[y-1][x+1] != target:
        return False
    if board[y][x+1] != target:
        return False
    return True

def check(board, x, y):
    # SE, SW, NE, NW
    result = ["SE","SW","NE", "NW"]
    if y == 0:
        # only check S
        result.remove("NE")
        result.remove("NW")
        if x == 0: 
            # only check E
            result.remove("SW")
            if not check_SE(board,x, y):
                result.remove("SE")
                
        elif x == len(board[0])-1: 
            # only check W
            result.remove("SE")
            if not check_SW(board,x, y):
                result.remove("SW")
        else:
            # check SE SW
            if not check_SE(board,x, y):
                result.remove("SE")
            if not check_SW(board,x, y):
                result.remove("SW")
    elif y == len(board)-1:
        # only check N
        result.remove("SE")
        result.remove("SW")
        if x == 0: 
            # only check E
            result.remove("NW")
            if not check_NE(board,x, y):
                result.remove("NE")
        elif x == len(board[0])-1: 
            # only check W
            result.remove("NE")
            if not check_NW(board,x, y):
                result.remove("NW")
        else:
            # check NE NW
            if not check_NE(board,x, y):
                result.remove("NE")
            if not check_NW(board,x, y):
                result.remove("NW")
    else:
        # check both N,S
        if x == 0: 
            # only check E
            result.remove("NW")
            result.remove("SW")
            if not check_NE(board, x, y):
                result.remove("NE")
            if not check_SE(board, x, y):
                result.remove("SE")
                
        elif x == len(board[0])-1: 
            # only check W
            result.remove("NE")
            result.remove("SE")
            if not check_NW(board, x, y):
                result.remove("NW")
            if not check_SW(board, x, y):
                result.remove("SW")
        else:
            if not check_NW(board, x, y):
                result.remove("NW")
            if not check_SW(board, x, y):
                result.remove("SW")
            if not check_NE(board, x, y):
                result.remove("NE")
            if not check_SE(board, x, y):
                result.remove("SE")
    return result
            
def find_four(board, m, n):
    results = []
    for y in range(m):
        for x in range(n):
            temp = []
            if board[y][x] != "^":
                check_result = check(board, x, y)
                if len(check_result) > 0:
                    # print(y, x, check_result)
                    results.append([y,x])
    # print(results)
    return results

def organize_board(board, targets):
    new_board = []
    # 1. get board in column wise
    cw_board = []
    for x in range(len(board[0])):
        temp = []
        for y in range(len(board)): 
            if [y, x] not in targets:
                temp.insert(0, board[y][x])
                #temp.append(board[y][x])
        if len(temp) != len(board[0]):
            cnt = len(board) - len(temp)
            for i in range(cnt):
                temp.append("^")
        cw_board.append(list(reversed(temp)))
    # print(cw_board)
    # 2. re-organize cw_style board to original style
    for y in range(len(board)):
        row = []
        for x in range(len(board[0])):
            row.append(cw_board[x][y])
        new_board.append(row)

    return new_board

def solution(m, n, board):
    answer = 0
    # m : 높이
    # n : 너비
    new_board =[]
    
    while True:
        # print(board)
        targets = find_four(board, m, n)
        if len(targets) > 0:
            answer += len(targets)
            board = organize_board(board, targets) 
            
        else:
            break
    
    return answer