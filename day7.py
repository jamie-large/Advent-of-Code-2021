def solution_part1():
    with open('inputs/day7.txt', 'r') as f:
        crabdict = {}
        crabset = set()
        for c in [int(x) for x in f.readline().split(',')]:
            crabdict[c] = crabdict.get(c, 0) + 1
            crabset.add(c)

        bestmin = float('inf')
        i = min(crabset)
        while i <= max(crabset):
            value = 0
            for h in crabdict:
                value += abs(h - i) * crabdict[h]
            if value < bestmin:
                bestmin = value
            i += 1
        print(bestmin)

def solution_part2():
    with open('inputs/day7.txt', 'r') as f:
        crabdict = {}
        crabset = set()
        for c in [int(x) for x in f.readline().split(',')]:
            crabdict[c] = crabdict.get(c, 0) + 1
            crabset.add(c)

        bestmin = float('inf')
        i = min(crabset)
        while i <= max(crabset):
            value = 0
            for h in crabdict:
                value += abs(h-i)*(abs(h - i) + 1) * 1/2 * crabdict[h]
            if value < bestmin:
                bestmin = value
            i += 1
        print(bestmin)

solution_part2()
