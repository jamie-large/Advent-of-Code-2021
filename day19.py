ROTATIONS = [('x', 'y', 'z'), ('z', 'y', '-x'), ('-x', 'y', '-z'), ('-z', 'y', 'x'), ('-x', '-y', 'z'), ('-z', '-y', '-x'),
             ('x', '-y', '-z'), ('z', '-y', 'x'), ('x', '-z', 'y'), ('y', '-z', '-x'), ('-x', '-z', '-y'), ('-y', '-z', 'x'),
             ('x', 'z', '-y'), ('-y', 'z', '-x'), ('-x', 'z', 'y'), ('y', 'z', 'x'), ('z', 'x', 'y'), ('y', 'x', '-z'),
             ('-z', 'x', '-y'), ('-y', 'x', 'z'), ('-z', '-x', 'y'), ('y', '-x', 'z'), ('z', '-x', '-y'), ('-y', '-x', '-z')]

def solution_part1():
    scanners = []
    with open('inputs/day19.txt', 'r') as f:
        current_scanner = None
        for line in f:
            if '---' in line:
                scanners.append([])
                current_scanner = scanners[-1]
            elif line != '\n':
                [x, y, z] = [int(n) for n in line[:-1].split(',')]
                current_scanner.append((x, y, z))

    # for each scanner, calculate distance between each pair of beacons
    scanner_distances = []
    for s in scanners:
        beacons = [dict() for _ in range(len(s))]
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                dist = distance(s[i], s[j])
                beacons[i][dist] = beacons[i].get(dist, 0) + 1
                beacons[j][dist] = beacons[j].get(dist, 0) + 1
        scanner_distances.append(beacons)

    # set of all the beacons relative to point 0
    final_beacons = set()
    for b in scanners[0]:
        final_beacons.add(b)

    iter = 0
    solved_scanners = [0]

    while iter < len(solved_scanners) and len(solved_scanners) < len(scanners):
        i = solved_scanners[iter]
        for j in range(len(scanner_distances)):
            if j == i or j in solved_scanners:
                continue
            es = equal_scanners(scanner_distances[i], scanner_distances[j])

            if len(es) == 12:
                for R in ROTATIONS:
                    difference = None

                    for (x, y) in es:
                        beacon1 = scanners[i][x]
                        beacon2 = make_rotation(R, scanners[j][y])

                        current_difference = (beacon2[0] - beacon1[0], beacon2[1] - beacon1[1], beacon2[2] - beacon1[2])

                        if difference is None:
                            difference = current_difference

                        if current_difference != difference:
                            break
                    else:
                        new_scanner = []
                        for b in scanners[j]:
                            rotated = make_rotation(R, b)
                            new_beacon = (rotated[0]-difference[0], rotated[1]-difference[1], rotated[2]-difference[2])
                            new_scanner.append(new_beacon)
                            final_beacons.add(new_beacon)
                        scanners[j] = new_scanner
                        if j not in solved_scanners:
                            solved_scanners.append(j)
                        break

        iter += 1

    print(len(final_beacons))

def distance(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2

def equal_scanners(s1, s2):
    beacon_pairs = set()
    for i in range(len(s1)):
        b1 = s1[i]
        for j in range(len(s2)):
            b2 = s2[j]
            count = 0
            for dist in b1:
                if dist in b2:
                    count += min(b1[dist], b2[dist])
                if count == 11:
                    beacon_pairs.add((i, j))
                    if len(beacon_pairs) == 12:
                        return beacon_pairs
    return []


def make_rotation(rotation, beacon):
    x, y, z = beacon
    if rotation[0] == '-x':
        x = beacon[0] * -1
    elif rotation[0] == 'y':
        x = beacon[1]
    elif rotation[0] == '-y':
        x = beacon[1] * -1
    elif rotation[0] == 'z':
        x = beacon[2]
    elif rotation[0] == '-z':
        x = beacon[2] * -1
    if rotation[1] == 'x':
        y = beacon[0]
    elif rotation[1] == '-x':
        y = beacon[0] * -1
    elif rotation[1] == '-y':
        y = beacon[1] * -1
    elif rotation[1] == 'z':
        y = beacon[2]
    elif rotation[1] == '-z':
        y = beacon[2] * -1
    if rotation[2] == 'x':
        z = beacon[0]
    elif rotation[2] == '-x':
        z = beacon[0] * -1
    elif rotation[2] == 'y':
        z = beacon[1]
    elif rotation[2] == '-y':
        z = beacon[1] * -1
    elif rotation[2] == '-z':
        z = beacon[2] * -1

    return (x, y, z)


def solution_part2():
    scanners = []
    with open('inputs/day19.txt', 'r') as f:
        current_scanner = None
        for line in f:
            if '---' in line:
                scanners.append([])
                current_scanner = scanners[-1]
            elif line != '\n':
                [x, y, z] = [int(n) for n in line[:-1].split(',')]
                current_scanner.append((x, y, z))

    # for each scanner, calculate distance between each pair of beacons
    scanner_distances = []
    for s in scanners:
        beacons = [dict() for _ in range(len(s))]
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                dist = distance(s[i], s[j])
                beacons[i][dist] = beacons[i].get(dist, 0) + 1
                beacons[j][dist] = beacons[j].get(dist, 0) + 1
        scanner_distances.append(beacons)

    # set of all the beacons relative to point 0
    final_beacons = set()
    for b in scanners[0]:
        final_beacons.add(b)

    iter = 0
    solved_scanners = [0]

    scanner_positions = set()
    scanner_positions.add((0,0,0))

    while iter < len(solved_scanners) and len(solved_scanners) < len(scanners):
        i = solved_scanners[iter]
        for j in range(len(scanner_distances)):
            if j == i or j in solved_scanners:
                continue
            es = equal_scanners(scanner_distances[i], scanner_distances[j])

            if len(es) == 12:
                for R in ROTATIONS:
                    difference = None

                    for (x, y) in es:
                        beacon1 = scanners[i][x]
                        beacon2 = make_rotation(R, scanners[j][y])

                        current_difference = (beacon2[0] - beacon1[0], beacon2[1] - beacon1[1], beacon2[2] - beacon1[2])

                        if difference is None:
                            difference = current_difference

                        if current_difference != difference:
                            break
                    else:
                        new_scanner = []
                        for b in scanners[j]:
                            rotated = make_rotation(R, b)
                            new_beacon = (rotated[0]-difference[0], rotated[1]-difference[1], rotated[2]-difference[2])
                            new_scanner.append(new_beacon)
                            final_beacons.add(new_beacon)
                        scanners[j] = new_scanner
                        if j not in solved_scanners:
                            solved_scanners.append(j)
                        scanner_positions.add((difference[0]*-1, difference[1]*-1, difference[2]*-1))
                        break

        iter += 1

    positions_list = list(scanner_positions)
    max_dist = 0
    for i in range(len(scanner_positions)):
        for j in range(i+1, len(scanner_positions)):
            dist = manhattan_distance(positions_list[i], positions_list[j])
            if dist > max_dist:
                max_dist = dist

    print(max_dist)

def manhattan_distance(b1, b2):
    return abs(b1[0] - b2[0]) + abs(b1[1] - b2[1]) + abs(b1[2] - b2[2])

solution_part2()
