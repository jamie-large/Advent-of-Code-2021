def solution_part1():
    with open('inputs/day8.txt', 'r') as f:
        result = 0
        for line in f:
            output_values = line.split()[-4:]
            for o in output_values:
                if len(o) == 2 or len(o) == 4 or len(o) == 3 or len(o) == 7:
                    result += 1
        print(result)

MAPPINGS = {
    'abcefg': '0',
    'cf': '1',
    'acdeg': '2',
    'acdfg': '3',
    'bcdf': '4',
    'abdfg': '5',
    'abdefg': '6',
    'acf': '7',
    'abcdefg': '8',
    'abcdfg': '9'
}

def solution_part2():
    with open('inputs/day8.txt', 'r') as f:
        result = 0
        for line in f:
            counts = {
                'a': 0,
                'b': 0,
                'c': 0,
                'd': 0,
                'e': 0,
                'f': 0,
                'g': 0
            }
            input_values = line.split()[:10]
            output_values = line.split()[-4:]
            one = None
            four = None
            seven = None
            for inp in input_values:
                if len(inp) == 2:
                    one = inp
                elif len(inp) == 3:
                    seven = inp
                elif len(inp) == 4:
                    four = inp
                for c in inp:
                    counts[c] += 1

            map = {}
            for c in counts:
                if counts[c] == 8 and c in seven and c not in one:
                    map[c] = 'a'
                elif counts[c] == 6:
                    map[c] = 'b'
                elif counts[c] == 8:
                    map[c] = 'c'
                elif counts[c] == 7 and c in four:
                    map[c] = 'd'
                elif counts[c] == 4:
                    map[c] = 'e'
                elif counts[c] == 9:
                    map[c] = 'f'
                elif counts[c] == 7:
                    map[c] = 'g'

            value = []
            for o in output_values:
                translation = [map[c] for c in o]
                translation.sort()
                translation_str = "".join(translation)
                value.append(MAPPINGS[translation_str])
            result += int("".join(value))


        print(result)

solution_part2()
