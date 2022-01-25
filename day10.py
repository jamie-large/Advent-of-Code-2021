MAPS = {
    ')': ('(', 3),
    ']': ('[', 57),
    '}': ('{', 1197),
    '>': ('<', 25137),
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}

def solution_part1():
    with open('inputs/day10.txt', 'r') as f:
        result = 0
        for line in f:
            stack = []
            for c in line:
                if c in ('(', '[', '{', '<'):
                    stack.append(c)
                    continue
                for m in MAPS:
                    if c == m:
                        if len(stack) == 0 or stack.pop() != MAPS[m][0]:
                            result += MAPS[m][1]
                            break
                else:
                    continue
                break
        print(result)


def solution_part2():
    with open('inputs/day10.txt', 'r') as f:
        scores = []
        for line in f:
            result = 0
            stack = []
            for c in line:
                if c in ('(', '[', '{', '<'):
                    stack.append(c)
                    continue
                for m in MAPS:
                    if c == m:
                        if len(stack) == 0 or stack.pop() != MAPS[m][0]:
                            break
                else:
                    continue
                break
            else:
                if len(stack) > 0:
                    while len(stack) > 0:
                        result *= 5
                        result += MAPS[stack.pop()]
                    scores.append(result)
        scores.sort()
        print(scores[int(len(scores) / 2)])

solution_part2()
