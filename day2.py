def solution_part1():
    with open('inputs/day2.txt', 'r') as f:
        position = 0
        depth = 0
        for line in f:
            [command, number] = line.split()
            if command == "forward":
                position += int(number)
            elif command == "down":
                depth += int(number)
            elif command == "up":
                depth -= int(number)
        print(position * depth)

def solution_part2():
    with open('inputs/day2.txt', 'r') as f:
        position = 0
        depth = 0
        aim = 0
        for line in f:
            [command, number] = line.split()
            if command == "forward":
                position += int(number)
                depth += aim * int(number)
            elif command == "down":
                aim += int(number)
            elif command == "up":
                aim -= int(number)
        print(position * depth)

solution_part2()
