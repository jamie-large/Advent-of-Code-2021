def solution_part1():
    with open('inputs/day11.txt', 'r') as f:
        octopi = [[int(c) for c in line[:-1]] for line in f.readlines()]
        flashes = 0
        for step in range(100):
            flashed = [[False for i in range(10)] for j in range(10)]
            for i in range(10):
                for j in range(10):
                    octopi[i][j] += 1
            for i in range(10):
                for j in range(10):
                    if octopi[i][j] > 9 and not flashed[i][j]:
                        flashed[i][j] = True
                        flashes += 1 + flash(i, j, octopi, flashed)
            for i in range(10):
                for j in range(10):
                    if flashed[i][j]:
                        octopi[i][j] = 0
        print(flashes)

def flash(x, y, octopi, flashed):
    result = 0
    neighbors = [(x+i, y+j) for i in (-1, 0, 1) for j in (-1, 0, 1)
                 if x+i >= 0 and y+j >= 0 and x+i < 10 and y+j < 10 and (i != 0 or j != 0)]
    for (i, j) in neighbors:
        octopi[i][j] += 1
        if octopi[i][j] > 9 and not flashed[i][j]:
            flashed[i][j] = True
            result += 1 + flash(i, j, octopi, flashed)
    return result

def solution_part2():
    with open('inputs/day11.txt', 'r') as f:
        octopi = [[int(c) for c in line[:-1]] for line in f.readlines()]
        step = 0
        while True:
            flashed = [[False for i in range(10)] for j in range(10)]
            for i in range(10):
                for j in range(10):
                    octopi[i][j] += 1
            for i in range(10):
                for j in range(10):
                    if octopi[i][j] > 9 and not flashed[i][j]:
                        flashed[i][j] = True
                        flash(i, j, octopi, flashed)
            for i in range(10):
                for j in range(10):
                    if flashed[i][j]:
                        octopi[i][j] = 0
            step += 1
            for i in range(10):
                for j in range(10):
                    if not flashed[i][j]:
                        break
                else:
                    continue
                break
            else:
                break
        print(step)

solution_part2()
