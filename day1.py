def solution_part1():
    with open('inputs/day1.txt', 'r') as f:
        result = 0
        previous_depth = -1
        for line in f:
            current_depth = int(line)
            if (previous_depth > 0 and current_depth > previous_depth):
                result += 1
            previous_depth = current_depth
        print(result)

def solution_part2():
    with open('inputs/day1.txt', 'r') as f:
        result = 0
        window = []
        i = 0
        for line in f:
            if len(window) < 3:
                window.append(int(line))
            else:
                previous_depth = sum(window)
                window[i] = int(line)
                if sum(window) > previous_depth:
                    result += 1
            i = (i + 1) % 3
        print(result)

solution_part2()
