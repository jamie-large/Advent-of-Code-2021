def solution_part1():
    with open('inputs/day13.txt', 'r') as f:
        points = set()
        folds = []
        for line in f:
            if ',' in line:
                [x, y] = [int(x) for x in line.split(',')]
                points.add((x,y))
            elif '=' in line:
                [dir, num] = line.split('=')
                folds.append((dir[-1], int(num)))
        for (dir, num) in folds:
            new_points = set()
            if dir == 'y':
                for (x,y) in points:
                    if y < num:
                        new_points.add((x,y))
                    elif y > num:
                        new_points.add((x, 2 * num - y))
            elif dir == 'x':
                for (x,y) in points:
                    if x < num:
                        new_points.add((x,y))
                    elif x > num:
                        new_points.add((2 * num - x, y))
            points = new_points
            print(len(points))
            break

def solution_part2():
    with open('inputs/day13.txt', 'r') as f:
        points = set()
        folds = []
        for line in f:
            if ',' in line:
                [x, y] = [int(x) for x in line.split(',')]
                points.add((x,y))
            elif '=' in line:
                [dir, num] = line.split('=')
                folds.append((dir[-1], int(num)))
        for (dir, num) in folds:
            new_points = set()
            if dir == 'y':
                for (x,y) in points:
                    if y < num:
                        new_points.add((x,y))
                    elif y > num:
                        new_points.add((x, 2 * num - y))
            elif dir == 'x':
                for (x,y) in points:
                    if x < num:
                        new_points.add((x,y))
                    elif x > num:
                        new_points.add((2 * num - x, y))
            points = new_points
        board = [['.' for i in range(100)] for i in range(100)]
        for (x, y) in points:
            board[x][y] = '#'
        for i in range(len(board) -1, -1, -1):
            print(''.join(board[i]))

solution_part2()
