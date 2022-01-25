def solution_part1():
    with open('inputs/day14.txt', 'r') as f:
        c = 0
        template = ""
        rules = {}
        for line in f:
            if c == 0:
                template = line[:-1]
            elif c > 1:
                [pair, insertion] = line.split(' -> ')
                rules[pair] = (pair[0] + insertion[:-1], insertion[:-1] + pair[1])
            c += 1

        pairs = {}
        for i in range(len(template) - 1):
            p = template[i] + template[i+1]
            pairs[p] = pairs.get(p, 0) + 1

        for i in range(10):
            new_pairs = {}
            for pair in pairs:
                for p in rules[pair]:
                    new_pairs[p] = new_pairs.get(p, 0) + pairs[pair]
            pairs = new_pairs

        counts = {}
        for pair in pairs:
            counts[pair[0]] = counts.get(pair[0], 0) + pairs[pair]
        counts[template[-1]] += 1

        print(max(counts.values()) - min(counts.values()))

def solution_part2():
    with open('inputs/day14.txt', 'r') as f:
        c = 0
        template = ""
        rules = {}
        for line in f:
            if c == 0:
                template = line[:-1]
            elif c > 1:
                [pair, insertion] = line.split(' -> ')
                rules[pair] = (pair[0] + insertion[:-1], insertion[:-1] + pair[1])
            c += 1

        pairs = {}
        for i in range(len(template) - 1):
            p = template[i] + template[i+1]
            pairs[p] = pairs.get(p, 0) + 1

        for i in range(40):
            new_pairs = {}
            for pair in pairs:
                for p in rules[pair]:
                    new_pairs[p] = new_pairs.get(p, 0) + pairs[pair]
            pairs = new_pairs

        counts = {}
        for pair in pairs:
            counts[pair[0]] = counts.get(pair[0], 0) + pairs[pair]
        counts[template[-1]] += 1

        print(max(counts.values()) - min(counts.values()))

solution_part2()
