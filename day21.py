def solution_part1():
    with open("inputs/day21.txt", "r") as f:
        position_1 = int(f.readline()[-2])
        position_2 = int(f.readline()[-2])

        roll = 1

        score_1 = 0
        score_2 = 0
        turn = 1

        rolls = 0

        while score_1 < 1000 and score_2 < 1000:
            if turn == 1:
                position_1 = (position_1 + roll + (roll % 100 + 1) + (roll % 100 + 2)) % 10
                score = 10 if position_1 == 0 else position_1
                score_1 += score
            else:
                position_2 = (position_2 + roll + (roll % 100 + 1) + (roll % 100 + 2)) % 10
                score = 10 if position_2 == 0 else position_2
                score_2 += score

            roll = ((roll + 2) % 100) + 1
            turn = 2 if turn == 1 else 1

            rolls += 3
        print(min(score_1, score_2))
        print(rolls)
        print(min(score_1, score_2) * rolls)

def solution_part2():
    with open("inputs/day21.txt", "r") as f:
        position_1 = int(f.readline()[-2])
        position_2 = int(f.readline()[-2])

        print(calculate_universes_1(position_1, position_2, 0, 0, 1))
        print(calculate_universes_2(position_1, position_2, 0, 0, 1))

universes_1 = {}
universes_2 = {}
ROLLS = {
    3: 1,
    4: 3,
    5: 6,
    6: 7,
    7: 6,
    8: 3,
    9: 1
}

def calculate_universes_1(position_1, position_2, score_1, score_2, turn):
    if score_1 >= 21:
        universes_1[(position_1, position_2, score_1, score_2, turn)] = 1
        return 1

    if score_2 >= 21:
        universes_1[(position_1, position_2, score_1, score_2, turn)] = 0
        return 0

    wins = 0
    for (roll, freq) in ROLLS.items():
        if turn == 1:
            new_position = (position_1 + roll) % 10
            score = 10 if new_position == 0 else new_position
            new_score = score_1 + score
            if (new_position, position_2, new_score, score_2, 2) not in universes_1:
                calculate_universes_1(new_position, position_2, new_score, score_2, 2)
            wins += freq * universes_1[(new_position, position_2, new_score, score_2, 2)]
        else:
            new_position = (position_2 + roll) % 10
            score = 10 if new_position == 0 else new_position
            new_score = score_2 + score
            if (position_1, new_position, score_1, new_score, 1) not in universes_1:
                calculate_universes_1(position_1, new_position, score_1, new_score, 1)
            wins += freq * universes_1[(position_1, new_position, score_1, new_score, 1)]

    universes_1[(position_1, position_2, score_1, score_2, turn)] = wins
    return wins

def calculate_universes_2(position_1, position_2, score_1, score_2, turn):
    if score_1 >= 21:
        universes_2[(position_1, position_2, score_1, score_2, turn)] = 0
        return 0

    if score_2 >= 21:
        universes_2[(position_1, position_2, score_1, score_2, turn)] = 1
        return 1

    wins = 0
    for (roll, freq) in ROLLS.items():
        if turn == 1:
            new_position = (position_1 + roll) % 10
            score = 10 if new_position == 0 else new_position
            new_score = score_1 + score
            if (new_position, position_2, new_score, score_2, 2) not in universes_2:
                calculate_universes_2(new_position, position_2, new_score, score_2, 2)
            wins += freq * universes_2[(new_position, position_2, new_score, score_2, 2)]
        else:
            new_position = (position_2 + roll) % 10
            score = 10 if new_position == 0 else new_position
            new_score = score_2 + score
            if (position_1, new_position, score_1, new_score, 1) not in universes_2:
                calculate_universes_2(position_1, new_position, score_1, new_score, 1)
            wins += freq * universes_2[(position_1, new_position, score_1, new_score, 1)]

    universes_2[(position_1, position_2, score_1, score_2, turn)] = wins
    return wins


solution_part2()
