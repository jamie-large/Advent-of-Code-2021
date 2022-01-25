def solution_part1():
    with open('inputs/day3.txt', 'r') as f:
        counter = None
        for line in f:
            if counter is None:
                counter = [0] * (len(line) - 1)
            for i in range(len(line)):
                if line[i] == '0':
                    counter[i] -= 1
                elif line[i] == '1':
                    counter[i] += 1
        epsilon = 0
        gamma = 0
        for i in range(len(counter)):
            if counter[i] > 0:
                epsilon += 2 ** (len(counter) - i - 1)
            elif counter[i] < 0:
                gamma += 2 ** (len(counter) - i - 1)
        print(epsilon * gamma)

def solution_part2():
    with open('inputs/day3.txt', 'r') as f:
        numbers = f.readlines()
        possible_02 = [i for i in range(len(numbers))]
        possible_C02 = [i for i in range(len(numbers))]

        for c in range(len(numbers[0])):
            if len(possible_02) > 1:
                count = 0
                for i in possible_02:
                    if numbers[i][c] == '1':
                        count += 1
                    elif numbers[i][c] == '0':
                        count -= 1
                match_02 = '1' if count >= 0 else '0'
                possible_02 = [i for i in possible_02 if numbers[i][c] == match_02]
                if c == 0:
                    match_C02 = '0' if count >= 0 else '1'
                    possible_C02 = [i for i in possible_C02 if numbers[i][c] == match_C02]
                    continue

            if len(possible_C02) > 1:
                count = 0
                for i in possible_C02:
                    if numbers[i][c] == '1':
                        count += 1
                    elif numbers[i][c] == '0':
                        count -= 1
                match_C02 = '0' if count >= 0 else '1'
                possible_C02 = [i for i in possible_C02 if numbers[i][c] == match_C02]

        print(possible_02)
        print(possible_C02)

        print(numbers[possible_02[0]])
        print(numbers[possible_C02[0]])

        print(int(numbers[possible_02[0]], 2) * int(numbers[possible_C02[0]], 2))


solution_part2()
