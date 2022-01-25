def solution_part1():
    with open('inputs/day6.txt', 'r') as f:
        numfish = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for f in [int(x) for x in f.readline().split(',')]:
            numfish[f] += 1

        for d in range(80):
            new_fish = numfish[0]
            for i in range(8):
                numfish[i] = numfish[i+1]
            numfish[6] += new_fish
            numfish[8] = new_fish

        print(sum(numfish))

def solution_part2():
    with open('inputs/day6.txt', 'r') as f:
        numfish = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for f in [int(x) for x in f.readline().split(',')]:
            numfish[f] += 1

        for d in range(256):
            new_fish = numfish[0]
            for i in range(8):
                numfish[i] = numfish[i+1]
            numfish[6] += new_fish
            numfish[8] = new_fish

        print(sum(numfish))


solution_part2()
