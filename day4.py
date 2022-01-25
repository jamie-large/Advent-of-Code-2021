def solution_part1():
    with open('inputs/day4.txt', 'r') as f:
        n = 0
        numbers_drawn = []
        boards = []
        for line in f:
            if numbers_drawn == []:
                numbers_drawn = [int(x) for x in line.split(',')]
                continue

            if n % 6 == 0:
                boards.append((set(), []))
            else:
                row = [int(x) for x in line.split()]
                for x in row:
                    boards[-1][0].add(x)
                boards[-1][1].append(row)

            n +=1

    for draw in numbers_drawn:
        for board in boards:
            if draw in board[0]:
                board[0].remove(draw)
                # mark the correct spot
                for i in range(5):
                    for j in range(5):
                        if board[1][i][j] == draw:
                            board[1][i][j] = -1
                            # Check if bingo
                            bingo = True
                            for k in range(5):
                                if board[1][i][k] != -1:
                                    bingo = False
                                    break
                            if not bingo:
                                bingo = True
                                for k in range(5):
                                    if board[1][k][j] != -1:
                                        bingo = False
                                        break
                            if bingo:
                                print(draw * sum(board[0]))
                                return
                            break
                    else:
                        continue
                    break

def solution_part2():
    with open('inputs/day4.txt', 'r') as f:
        n = 0
        numbers_drawn = []
        boards = []
        for line in f:
            if numbers_drawn == []:
                numbers_drawn = [int(x) for x in line.split(',')]
                continue

            if n % 6 == 0:
                boards.append((set(), []))
            else:
                row = [int(x) for x in line.split()]
                for x in row:
                    boards[-1][0].add(x)
                boards[-1][1].append(row)

            n +=1

    for draw in numbers_drawn:
        topop = []
        for b in range(len(boards)):
            if draw in boards[b][0]:
                boards[b][0].remove(draw)
                # mark the correct spot
                for i in range(5):
                    for j in range(5):
                        if boards[b][1][i][j] == draw:
                            boards[b][1][i][j] = -1
                            # Check if bingo
                            bingo = True
                            for k in range(5):
                                if boards[b][1][i][k] != -1:
                                    bingo = False
                                    break
                            if not bingo:
                                bingo = True
                                for k in range(5):
                                    if boards[b][1][k][j] != -1:
                                        bingo = False
                                        break
                            if bingo:
                                if len(boards) == 1:
                                    print(draw * sum(boards[0][0]))
                                    return
                                topop.append(b)
                            break
                    else:
                        continue
                    break
        topop.reverse()
        for p in topop:
            boards.pop(p)

solution_part2()
