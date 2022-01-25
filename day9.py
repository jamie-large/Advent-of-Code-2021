def solution_part1():
    with open('inputs/day9.txt', 'r') as f:
        result = 0
        lines = []
        for line in f:
            lines.append([int(x) for x in list(line)[:-1]])
            if len(lines) == 1:
                continue

            elif len(lines) == 2:
                if lines[0][0] < lines[0][1] and lines[0][0] < lines[1][0]:
                    result += lines[0][0] + 1
                if lines[0][len(lines[0]) - 1] < lines[0][len(lines[0]) - 2] and \
                   lines[0][len(lines[0]) - 1] < lines[1][len(lines[0]) - 1]:
                    result += lines[0][len(lines[0]) - 1] + 1
                for i in range(1, len(lines[0]) - 1):
                    if lines[0][i] < lines[0][i - 1] and lines[0][i] < lines[0][i + 1] and lines[0][i] < lines[1][i]:
                        result += lines[0][i] + 1
                continue

            if len(lines) == 4:
                lines.pop(0)

            if lines[1][0] < lines[1][1] and lines[1][0] < lines[2][0] and lines[1][0] < lines[0][0]:
                result += lines[1][0] + 1
            if lines[1][len(lines[0]) - 1] < lines[1][len(lines[0]) - 2] and \
               lines[1][len(lines[0]) - 1] < lines[2][len(lines[0]) - 1] and \
               lines[1][len(lines[0]) - 1] < lines[0][len(lines[0]) - 1]:
                result += lines[1][len(lines[0]) - 1] + 1
            for i in range(1, len(lines[1]) - 1):
                if lines[1][i] < lines[1][i - 1] and lines[1][i] < lines[1][i + 1] and \
                   lines[1][i] < lines[2][i] and lines[1][i] < lines[0][i]:
                    result += lines[1][i] + 1

        if lines[2][0] < lines[2][1] and lines[2][0] < lines[1][0]:
            result += lines[2][0] + 1
        if lines[2][len(lines[0]) - 1] < lines[2][len(lines[0]) - 2] and \
           lines[2][len(lines[0]) - 1] < lines[1][len(lines[0]) - 1]:
            result += lines[2][len(lines[0]) - 1] + 1
        for i in range(1, len(lines[0]) - 1):
            if lines[2][i] < lines[2][i - 1] and lines[2][i] < lines[2][i + 1] and lines[2][i] < lines[1][i]:
                result += lines[2][i] + 1

        print(result)

def solution_part2():
    with open('inputs/day9.txt', 'r') as f:
        grid = [[int(x) for x in line[:-1]] for line in f.readlines()]
        basins = [[None] * len(grid[0]) for i in range(len(grid))]
        basin_sizes = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 9 and basins[i][j] is None:
                    basin_sizes.append(0)
                    DFS(i, j, grid, basins, basin_sizes)
        basin_sizes.sort()
        print(basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3])

def DFS(i, j, grid, basins, basin_sizes):
    basins[i][j] = len(basin_sizes) - 1
    basin_sizes[-1] += 1

    neighbors = [(x, y) for (x, y) in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)] \
                 if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0])]

    for (x, y) in neighbors:
        if grid[x][y] != 9 and basins[x][y] is None:
            DFS(x, y, grid, basins, basin_sizes)

solution_part2()
