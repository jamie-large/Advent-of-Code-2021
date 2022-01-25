def solution_part1():
    locations = {}
    result = 0
    with open('inputs/day5.txt', 'r') as f:
        for line in f:
            [x1, y1, x2, y2] = [int(x) for x in line.replace('->', ',').split(',')]
            if x1 == x2:
                for i in range(min(y1, y2), max(y1, y2) + 1):
                    locations[(x1, i)] = locations.get((x1, i), 0) + 1
                    if locations[(x1, i)] == 2:
                        result += 1
            if y1 == y2:
                for i in range(min(x1, x2), max(x1, x2) + 1):
                    locations[(i, y1)] = locations.get((i, y1), 0) + 1
                    if locations[(i, y1)] == 2:
                        result += 1
    print(result)

def solution_part2():
    locations = {}
    result = 0
    with open('inputs/day5.txt', 'r') as f:
        for line in f:
            [x1, y1, x2, y2] = [int(x) for x in line.replace('->', ',').split(',')]
            if x1 == x2:
                for i in range(min(y1, y2), max(y1, y2) + 1):
                    locations[(x1, i)] = locations.get((x1, i), 0) + 1
                    if locations[(x1, i)] == 2:
                        result += 1
            elif y1 == y2:
                for i in range(min(x1, x2), max(x1, x2) + 1):
                    locations[(i, y1)] = locations.get((i, y1), 0) + 1
                    if locations[(i, y1)] == 2:
                        result += 1
            else:
                x_dir = 1 if x2 > x1 else -1
                y_dir = 1 if y2 > y1 else -1
                for i in range(max(x1, x2) - min(x1, x2) + 1):
                    locations[(x1 + i * x_dir, y1 + i * y_dir)] = locations.get((x1 + i * x_dir, y1 + i * y_dir), 0) + 1
                    if locations[(x1 + i * x_dir, y1 + i * y_dir)] == 2:
                        result += 1
    print(result)


solution_part2()
