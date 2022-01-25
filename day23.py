COSTS = {
    "A": 1,
    "B": 10,
    "C": 100,
    "D": 1000
}

amphipods = ["A", "B", "C", "D"]

def solution_part1():
    hallway = ["."] * 11
    buckets = [[".", "."] for _ in range(4)]
    with open('inputs/day23.txt', 'r') as f:
        text = f.readlines()
        for i in range(4):
            buckets[i][0] = text[2][i*2 + 3]
            buckets[i][1] = text[3][i*2 + 3]

    initial_state = stringify(hallway, buckets)
    states = {}
    states[initial_state] = 0
    queue = set()
    visited = set()

    queue.add(initial_state)
    while queue:
        # get minimum node
        min_value = float('inf')
        min_node = None
        for s in queue:
            if states[s] < min_value:
                min_value = states[s]
                min_node = s

        queue.remove(min_node)
        visited.add(min_node)
        hallway, buckets = destringify_1(min_node)

        cost = states[stringify(hallway, buckets)]

        if min_node == "...........AABBCCDD":
            print("FOUND IT!!!")
            print(f"COST: {cost}")
            return

        new_states = []
        # case 1: moving from bucket to hallway (freezes everything in hallway)
        for i in range(4):
            # from top of bucket
            if buckets[i][0] != "." and (buckets[i][0] != amphipods[i] or buckets[i][1] != amphipods[i]):
                for d in (i*2+1, i*2+3):
                    if hallway[d] == ".":
                        new_hallway = [(i + "x" if len(i) == 1 and i != "." else i) for i in hallway]
                        new_buckets = [[i for i in b] for b in buckets]
                        new_hallway[d] = buckets[i][0]
                        new_buckets[i][0] = "."
                        new_states.append((stringify(new_hallway, new_buckets), cost + COSTS[buckets[i][0]] * 2))

            # from bottom of bucket
            if buckets[i][0] == "." and buckets[i][1] != "." and buckets[i][1] != amphipods[i]:
                for d in (i*2+1, i*2+3):
                    if hallway[d] == ".":
                        new_hallway = [(i + "x" if len(i) == 1 and i != "." else i) for i in hallway]
                        new_buckets = [[i for i in b] for b in buckets]
                        new_hallway[d] = buckets[i][1]
                        new_buckets[i][1] = "."
                        new_states.append((stringify(new_hallway, new_buckets), cost + COSTS[buckets[i][1]] * 3))

        # case 2: moving around hallway (not frozen)
        for i in (0, 9):
            # move one space to right
            if hallway[i] != "." and len(hallway[i]) == 1 and hallway[i+1] == ".":
                new_hallway = [i for i in hallway]
                new_hallway[i+1] = hallway[i]
                new_hallway[i] = "."
                new_states.append((stringify(new_hallway, buckets), cost + COSTS[hallway[i]]))
        for i in (1, 10):
            # move one space to left
            if hallway[i] != "." and len(hallway[i]) == 1 and hallway[i-1] == ".":
                new_hallway = [i for i in hallway]
                new_hallway[i-1] = hallway[i]
                new_hallway[i] = "."
                new_states.append((stringify(new_hallway, buckets), cost + COSTS[hallway[i]]))
        for i in (1, 3, 5, 7):
            # move two spaces to right
            if hallway[i] != "." and len(hallway[i]) == 1 and hallway[i+2] == ".":
                new_hallway = [i for i in hallway]
                new_hallway[i+2] = hallway[i]
                new_hallway[i] = "."
                new_states.append((stringify(new_hallway, buckets), cost + COSTS[hallway[i]] * 2))
        for i in (3, 5, 7, 9):
            # move two spaces to left
            if hallway[i] != "." and len(hallway[i]) == 1 and hallway[i-2] == ".":
                new_hallway = [i for i in hallway]
                new_hallway[i-2] = hallway[i]
                new_hallway[i] = "."
                new_states.append((stringify(new_hallway, buckets), cost + COSTS[hallway[i]] * 2))

        # case 3: moving into bucket
        for i in range(4):
            # move into bottom of bucket
            if buckets[i][1] == ".":
                for d in (i*2+1, i*2+3):
                    if hallway[d] == amphipods[i]:
                        new_hallway = [i for i in hallway]
                        new_buckets = [[i for i in b] for b in buckets]
                        new_buckets[i][1] = hallway[d]
                        new_hallway[d] = "."
                        new_states.append((stringify(new_hallway, new_buckets), cost + COSTS[hallway[d]] * 3))
            # move into top of bucket
            if buckets[i][1] == amphipods[i] and buckets[i][0] == ".":
                for d in (i*2+1, i*2+3):
                    if hallway[d] == amphipods[i]:
                        new_hallway = [i for i in hallway]
                        new_buckets = [[i for i in b] for b in buckets]
                        new_buckets[i][0] = hallway[d]
                        new_hallway[d] = "."
                        new_states.append((stringify(new_hallway, new_buckets), cost + COSTS[hallway[d]] * 2))

        # case 4: move frozen into bucket
        for i in range(11):
            if hallway[i][-1] == "x":
                destination_bucket = amphipods.index(hallway[i][0])
                destination_index = destination_bucket * 2 + 2
                if buckets[destination_bucket][1] not in (".", amphipods[destination_bucket]) or \
                buckets[destination_bucket][0] != ".":
                    continue
                for j in range(min(destination_index, i), max(destination_index, i) + 1):
                    if hallway[j] != "." and j != i:
                        break
                else:
                    d = 1 if buckets[destination_bucket][1] == "." else 0
                    new_hallway = [(i + "x" if len(i) == 1 and i != "." else i) for i in hallway]
                    new_buckets = [[i for i in b] for b in buckets]
                    new_buckets[destination_bucket][d] = hallway[i][0]
                    new_hallway[i] = "."
                    steps = abs(destination_index - i) + d + 1
                    new_states.append((stringify(new_hallway, new_buckets), cost + COSTS[hallway[i][0]] * steps))

        for new_state, new_cost in new_states:
            if new_state in visited:
                continue
            if new_cost < states.get(new_state, float('inf')):
                states[new_state] = new_cost
            queue.add(new_state)

        print(f"Visited {len(visited)}, Queue has {len(queue)}")

def stringify(hallway, buckets):
    return "".join(hallway) + "".join(["".join(bucket) for bucket in buckets])

def destringify_1(code):
    i = 0
    hallway = []
    while len(hallway) < 11:
        if code[i] == ".":
            hallway.append(".")
        else:
            if code[i+1] == "x":
                hallway.append(code[i] + code[i+1])
                i += 1
            else:
                hallway.append(code[i])
        i += 1
    buckets = [[".","."] for _ in range(4)]
    for j in range(4):
        for k in range(2):
            buckets[j][k] = code[i]
            i += 1
    return hallway, buckets

def destringify_2(code):
    i = 0
    hallway = []
    while len(hallway) < 11:
        if code[i] == ".":
            hallway.append(".")
        else:
            if code[i+1] == "x":
                hallway.append(code[i] + code[i+1])
                i += 1
            else:
                hallway.append(code[i])
        i += 1
    buckets = [[".",".",".","."] for _ in range(4)]
    for j in range(4):
        for k in range(4):
            buckets[j][k] = code[i]
            i += 1
    return hallway, buckets


def solution_part2():
    hallway = ["."] * 11
    buckets = [[".", ".", ".", "."] for _ in range(4)]
    with open('inputs/day23.txt', 'r') as f:
        text = f.readlines()
        for i in range(4):
            buckets[i][0] = text[2][i*2 + 3]
            buckets[i][1] = text[3][i*2 + 3]
            buckets[i][2] = text[4][i*2 + 3]
            buckets[i][3] = text[5][i*2 + 3]

    initial_state = stringify(hallway, buckets)
    states = {}
    states[initial_state] = 0
    queue = set()
    visited = set()

    queue.add(initial_state)
    while queue:
        # get minimum node
        min_value = float('inf')
        min_node = None
        for s in queue:
            if states[s] < min_value:
                min_value = states[s]
                min_node = s

        queue.remove(min_node)
        visited.add(min_node)
        hallway, buckets = destringify_2(min_node)

        cost = states[stringify(hallway, buckets)]


        if min_node == "...........AAAABBBBCCCCDDDD":
            print("FOUND IT!!!")
            print(f"It only took {len(visited)} tries")
            print(f"COST: {cost}")
            return

        new_states = []
        # case 1: moving from bucket to hallway (freezes everything in hallway)
        for i in range(4):
            # from top of bucket
            if buckets[i][0] != "." and (buckets[i][0] != amphipods[i] or buckets[i][1] != amphipods[i] or \
                                         buckets[i][2] != amphipods[i] or buckets[i][3] != amphipods[i]):
                for d in (i*2+1, i*2+3):
                    if hallway[d] == ".":
                        new_hallway = [(i + "x" if len(i) == 1 and i != "." else i) for i in hallway]
                        new_buckets = [[i for i in b] for b in buckets]
                        new_hallway[d] = buckets[i][0]
                        new_buckets[i][0] = "."
                        new_states.append((stringify(new_hallway, new_buckets), cost + COSTS[buckets[i][0]] * 2))

            # from second part of bucket
            if buckets[i][0] == "." and buckets[i][1] != "." and \
                (buckets[i][1] != amphipods[i] or buckets[i][2] != amphipods[i] or buckets[i][3] != amphipods[i]):
                for d in (i*2+1, i*2+3):
                    if hallway[d] == ".":
                        new_hallway = [(i + "x" if len(i) == 1 and i != "." else i) for i in hallway]
                        new_buckets = [[i for i in b] for b in buckets]
                        new_hallway[d] = buckets[i][1]
                        new_buckets[i][1] = "."
                        new_states.append((stringify(new_hallway, new_buckets), cost + COSTS[buckets[i][1]] * 3))

            # from third part of bucket
            if buckets[i][0] == "." and buckets[i][1] == "." and buckets[i][2] != "." and \
                (buckets[i][2] != amphipods[i] or buckets[i][3] != amphipods[i]):
                for d in (i*2+1, i*2+3):
                    if hallway[d] == ".":
                        new_hallway = [(i + "x" if len(i) == 1 and i != "." else i) for i in hallway]
                        new_buckets = [[i for i in b] for b in buckets]
                        new_hallway[d] = buckets[i][2]
                        new_buckets[i][2] = "."
                        new_states.append((stringify(new_hallway, new_buckets), cost + COSTS[buckets[i][2]] * 4))

            # from fourth part of bucket
            if buckets[i][0] == "." and buckets[i][1] == "." and buckets[i][2] == "." and \
                buckets[i][3] != "." and buckets[i][3] != amphipods[i]:
                for d in (i*2+1, i*2+3):
                    if hallway[d] == ".":
                        new_hallway = [(i + "x" if len(i) == 1 and i != "." else i) for i in hallway]
                        new_buckets = [[i for i in b] for b in buckets]
                        new_hallway[d] = buckets[i][3]
                        new_buckets[i][3] = "."
                        new_states.append((stringify(new_hallway, new_buckets), cost + COSTS[buckets[i][3]] * 5))

        # case 2: moving around hallway (not frozen)
        for i in (0, 9):
            # move one space to right
            if hallway[i] != "." and len(hallway[i]) == 1 and hallway[i+1] == ".":
                new_hallway = [i for i in hallway]
                new_hallway[i+1] = hallway[i]
                new_hallway[i] = "."
                new_states.append((stringify(new_hallway, buckets), cost + COSTS[hallway[i]]))
        for i in (1, 10):
            # move one space to left
            if hallway[i] != "." and len(hallway[i]) == 1 and hallway[i-1] == ".":
                new_hallway = [i for i in hallway]
                new_hallway[i-1] = hallway[i]
                new_hallway[i] = "."
                new_states.append((stringify(new_hallway, buckets), cost + COSTS[hallway[i]]))
        for i in (1, 3, 5, 7):
            # move two spaces to right
            if hallway[i] != "." and len(hallway[i]) == 1 and hallway[i+2] == ".":
                new_hallway = [i for i in hallway]
                new_hallway[i+2] = hallway[i]
                new_hallway[i] = "."
                new_states.append((stringify(new_hallway, buckets), cost + COSTS[hallway[i]] * 2))
        for i in (3, 5, 7, 9):
            # move two spaces to left
            if hallway[i] != "." and len(hallway[i]) == 1 and hallway[i-2] == ".":
                new_hallway = [i for i in hallway]
                new_hallway[i-2] = hallway[i]
                new_hallway[i] = "."
                new_states.append((stringify(new_hallway, buckets), cost + COSTS[hallway[i]] * 2))

        # case 3: moving into bucket
        for i in range(4):
            # move into bottom of bucket
            if buckets[i][3] == ".":
                for d in (i*2+1, i*2+3):
                    if hallway[d] == amphipods[i]:
                        new_hallway = [i for i in hallway]
                        new_buckets = [[i for i in b] for b in buckets]
                        new_buckets[i][3] = hallway[d]
                        new_hallway[d] = "."
                        new_states.append((stringify(new_hallway, new_buckets), cost + COSTS[hallway[d]] * 5))
            # move into 3rd slot
            if buckets[i][2] == "." and buckets[i][3] == amphipods[i]:
                for d in (i*2+1, i*2+3):
                    if hallway[d] == amphipods[i]:
                        new_hallway = [i for i in hallway]
                        new_buckets = [[i for i in b] for b in buckets]
                        new_buckets[i][2] = hallway[d]
                        new_hallway[d] = "."
                        new_states.append((stringify(new_hallway, new_buckets), cost + COSTS[hallway[d]] * 4))
            # move into second slot
            if buckets[i][1] == "." and buckets[i][2] == amphipods[i] and buckets[i][3] == amphipods[i]:
                for d in (i*2+1, i*2+3):
                    if hallway[d] == amphipods[i]:
                        new_hallway = [i for i in hallway]
                        new_buckets = [[i for i in b] for b in buckets]
                        new_buckets[i][1] = hallway[d]
                        new_hallway[d] = "."
                        new_states.append((stringify(new_hallway, new_buckets), cost + COSTS[hallway[d]] * 3))
            # move into top of bucket
            if buckets[i][0] == "." and buckets[i][1] == amphipods[i] and buckets[i][2] == amphipods[i] and buckets[i][3] == amphipods[i]:
                for d in (i*2+1, i*2+3):
                    if hallway[d] == amphipods[i]:
                        new_hallway = [i for i in hallway]
                        new_buckets = [[i for i in b] for b in buckets]
                        new_buckets[i][0] = hallway[d]
                        new_hallway[d] = "."
                        new_states.append((stringify(new_hallway, new_buckets), cost + COSTS[hallway[d]] * 2))

        # case 4: move frozen into bucket
        for i in range(11):
            if hallway[i][-1] == "x":
                destination_bucket = amphipods.index(hallway[i][0])
                destination_index = destination_bucket * 2 + 2
                if buckets[destination_bucket][3] not in (".", amphipods[destination_bucket]) or \
                   buckets[destination_bucket][2] not in (".", amphipods[destination_bucket]) or \
                   buckets[destination_bucket][1] not in (".", amphipods[destination_bucket]) or \
                   buckets[destination_bucket][0] != ".":
                    continue
                for j in range(min(destination_index, i), max(destination_index, i) + 1):
                    if hallway[j] != "." and j != i:
                        break
                else:
                    d = 3 if buckets[destination_bucket][3] == "." else \
                        2 if buckets[destination_bucket][2] == "." else \
                        1 if buckets[destination_bucket][1] == "." else 0
                    new_hallway = [(i + "x" if len(i) == 1 and i != "." else i) for i in hallway]
                    new_buckets = [[i for i in b] for b in buckets]
                    new_buckets[destination_bucket][d] = hallway[i][0]
                    new_hallway[i] = "."
                    steps = abs(destination_index - i) + d + 1
                    new_states.append((stringify(new_hallway, new_buckets), cost + COSTS[hallway[i][0]] * steps))

        for new_state, new_cost in new_states:
            if new_state in visited:
                continue
            if new_cost < states.get(new_state, float('inf')):
                states[new_state] = new_cost
            queue.add(new_state)

        if (len(visited) % 1000 == 0):
            print(f"Visited {len(visited)}, Queue has {len(queue)}")


solution_part2()
