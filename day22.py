def solution_part1():
    with open("inputs/day22.txt", "r") as f:
        switches_on = set()
        for line in f:
            instruction = "on" if line[:2] == "on" else "off"
            bounds = [[int(x) for x in s[2:].split("..")] for s in line[len(instruction) + 1:-1].split(",")]

            for i in range(max(bounds[0][0], -50), min(bounds[0][1] + 1, 51)):
                for j in range(max(bounds[1][0], -50), min(bounds[1][1] + 1, 51)):
                    for k in range(max(bounds[2][0], -50), min(bounds[2][1] + 1, 51)):
                        if instruction == "on":
                            switches_on.add((i, j, k))
                        elif (i, j, k) in switches_on:
                            switches_on.remove((i, j, k))

            print(len(switches_on))

def solution_part2():
    with open("inputs/day22.txt", "r") as f:
        on_regions = []
        for line in f:
            instruction = "on" if line[:2] == "on" else "off"
            bounds = [[int(x) for x in s[2:].split("..")] for s in line[len(instruction) + 1:-1].split(",")]
            if instruction == "on":
                new_regions = [bounds]
                i = 0
                while i < len(new_regions):
                    r = new_regions[i]
                    for on_r in on_regions:
                        over = overlap(r, on_r)
                        if over != []:
                            new_regions = new_regions + subtract_regions(r, over)
                            del new_regions[i]
                            i -= 1
                            break
                    i += 1
                on_regions = on_regions + new_regions
            else:
                i = 0
                while i < len(on_regions):
                    r = on_regions[i]
                    over = overlap(bounds, r)
                    if over != []:
                        new_regions = subtract_regions(r, over)
                        del on_regions[i]
                        on_regions = new_regions + on_regions
                        i += len(new_regions) - 1
                    i += 1

        result = 0
        for r in on_regions:
            result += area(r)

        print(result)

def area(r):
    return (r[0][1] - r[0][0] + 1) * (r[1][1] - r[1][0] + 1) * (r[2][1] - r[2][0] + 1)

def overlap(region1, region2):
    if max(region1[0][0], region2[0][0]) > min(region1[0][1], region2[0][1]) or \
       max(region1[1][0], region2[1][0]) > min(region1[1][1], region2[1][1]) or \
       max(region1[2][0], region2[2][0]) > min(region1[2][1], region2[2][1]):
       return []

    return [[max(region1[0][0], region2[0][0]), min(region1[0][1], region2[0][1])],
            [max(region1[1][0], region2[1][0]), min(region1[1][1], region2[1][1])],
            [max(region1[2][0], region2[2][0]), min(region1[2][1], region2[2][1])]]

def subtract_regions(region1, region2):
    x_areas = [region2[0]]
    y_areas = [region2[1]]
    z_areas = [region2[2]]

    for i in range(3):
        area = x_areas if i == 0 else y_areas if i == 1 else z_areas
        if region1[i][0] < region2[i][0]:
            area.append([region1[i][0], region2[i][0] - 1])
        if region1[i][1] > region2[i][1]:
            area.append([region2[i][1] + 1, region1[i][1]])

    regions = [[x, y, z] for x in x_areas for y in y_areas for z in z_areas \
                         if (x != region2[0] or y != region2[1] or z != region2[2])]

    return regions


solution_part2()
