def check_SE(board, x, y):
    # helper function for functinon "check"
    # check if neighbor blocks of board[y,x]
    # that are placed in South East side of board[y,x]
    # are part of "Friends 4 Block"
    
    # return True if they are part of "Friends 4 Block"
    # else return False
    target = board[y][x] 
    if board[y][x+1] != target:
        return False
    if board[y+1][x+1] != target:
        return False
    if board[y+1][x] != target:
        return False
    return True

def check_SW(board, x, y):
    # helper function for functinon "check"
    # check if neighbor blocks of board[y,x]
    # that are placed in South West side of board[y,x]
    # are part of "Friends 4 Block"
    
    # return True if they are part of "Friends 4 Block"
    # else return False
    target = board[y][x]
    if board[y][x-1] != target:
        return False
    if board[y+1][x] != target:
        return False
    if board[y+1][x-1] != target:
        return False
    return True

def check_NW(board, x, y):
    # helper function for functinon "check"
    # check if neighbor blocks of board[y,x]
    # that are placed in North West side of board[y,x]
    # are part of "Friends 4 Block"
    
    # return True if they are part of "Friends 4 Block"
    # else return False
    target = board[y][x]
    if board[y-1][x] != target:
        return False
    if board[y-1][x-1] != target:
        return False
    if board[y][x-1] != target:
        return False
    return True

def check_NE(board, x, y):
    # helper function for functinon "check"
    # check if neighbor blocks of board[y,x]
    # that are placed in North East side of board[y,x]
    # are part of "Friends 4 Block"
    
    # return True if they are part of "Friends 4 Block"
    # else return False
    target = board[y][x]
    if board[y-1][x] != target:
        return False
    if board[y-1][x+1] != target:
        return False
    if board[y][x+1] != target:
        return False
    return True

def check(board, x, y):
    # helper functino for function "find_four"
    # check if block, board[y,x], counts as "Friend 4 Block"
    # return list of "Friend 4 Block"s that board[y,x] are part of
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
    # function that returns the list of blocks, board[y][x], that are 
    # count as "Friend 4 Block"
    
    results = []
    for y in range(m):
        for x in range(n):
            temp = []
            # avoid to check empty block board[y][x] == "^"
            if board[y][x] != "^":
                check_result = check(board, x, y)
                if len(check_result) > 0:
                    results.append([y,x])
    return results

def organize_board(board, targets):
    # organize the board in a way that there exist no space between blocks
    # in terms of vertical axis(column-wise) 
    # return organized board
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
        
    # 2. re-organize cw_style board to original style
    for y in range(len(board)):
        row = []
        for x in range(len(board[0])):
            row.append(cw_board[x][y])
        new_board.append(row)

    return new_board

def solution(m, n, board):
    answer = 0
    
    while True:
        # find blocks that are counted as part of "Friends 4 Block"
        # targets: list of vectors that contains [y,x]
        targets = find_four(board, m, n)
        if len(targets) > 0:
            answer += len(targets)
            # organize the board in a way that there exist no space between blocks
            # in terms of vertical axis(column-wise)
            board = organize_board(board, targets) 
            
        else:
            # if there exists no block that are "Friends 4 Block",
            # terminate the while loop
            break
    
    return answer
