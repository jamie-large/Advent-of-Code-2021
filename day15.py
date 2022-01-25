def solution_part1():
    with open('inputs/day15.txt', 'r') as f:
        board = [[int(x) for x in line[:-1]] for line in f.readlines()]
        costs = [[float('inf') for _ in range(len(board[0]))] for _ in range(len(board))]
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        visiting = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        costs[0][0] = 0

        queue = [(0,0)]

        while not visited[-1][-1]:
            [x, y] = queue.pop(get_min_index(queue, costs))
            neighbors = [(x+i, y+j) for (i, j) in [(0, 1), (0, -1), (-1, 0), (1, 0)]
                        if x+i >= 0 and x+i < len(board) and y+j >= 0 and y+j < len(board[0]) and not visited[x+i][y+j]]
            for (i, j) in neighbors:
                if costs[x][y] + board[i][j] < costs[i][j]:
                    costs[i][j] = costs[x][y] + board[i][j]
                if not visiting[i][j]:
                    queue.append((i, j))
                    visiting[i][j] = True
            visited[x][y] = True

        print(costs[-1][-1])

def get_min_index(queue, costs):
    min_cost = float('inf')
    result = None
    for i in range(len(queue)):
        [x, y] = queue[i]
        if costs[x][y] < min_cost:
            min_cost = costs[x][y]
            result = i
    return result

def solution_part2():
    with open('inputs/day15.txt', 'r') as f:
        board = [[int(x) for x in line[:-1]] for line in f.readlines()]
        new_board = []
        for line in board:
            new_line = line[:]
            for i in range(4):
                new_line += [((x+i) % 9) + 1 for x in line]
            new_board.append(new_line)
        board = new_board[:]
        for i in range(4):
            for line in board:
                new_board.append([((x+i) % 9) + 1 for x in line])

        board = new_board

        costs = [[float('inf') for _ in range(len(board[0]))] for _ in range(len(board))]
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        visiting = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        costs[0][0] = 0

        queue = [(0,0)]

        while not visited[-1][-1]:
            [x, y] = queue.pop(get_min_index(queue, costs))
            neighbors = [(x+i, y+j) for (i, j) in [(0, 1), (0, -1), (-1, 0), (1, 0)]
                        if x+i >= 0 and x+i < len(board) and y+j >= 0 and y+j < len(board[0]) and not visited[x+i][y+j]]
            for (i, j) in neighbors:
                if costs[x][y] + board[i][j] < costs[i][j]:
                    costs[i][j] = costs[x][y] + board[i][j]
                if not visiting[i][j]:
                    queue.append((i, j))
                    visiting[i][j] = True
            visited[x][y] = True

        print(costs[-1][-1])

solution_part2()
