def solution(board, moves):
    answer = 0
    row = len(board)
    col = len(board[0])
    
    bucket = []
    valid_move = len(moves)
    for move in moves:
        catch = False
        for i in range(row):
            target = board[i][move-1]
            if target != 0:
                board[i][move-1] = 0
                if len(bucket) != 0 and bucket[-1] == target:
                    bucket.pop()
                else:
                    bucket.append(target)
                catch = True
                break
        if not catch:
            valid_move -=1
    
    return valid_move - len(bucket)
    
        