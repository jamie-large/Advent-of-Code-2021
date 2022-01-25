def solution_part1():
    with open('inputs/day12.txt', 'r') as f:
        graph = {}
        for line in f:
            [origin, destination] = line[:-1].split('-')
            if origin not in graph:
                graph[origin] = []
            if destination not in graph:
                graph[destination] = []
            graph[origin].append(destination)
            graph[destination].append(origin)

        result = 0
        paths = [['start']]
        while len(paths) > 0:
            current = paths.pop(0)
            for neighbor in graph[current[-1]]:
                if neighbor == 'end':
                    result += 1
                elif neighbor.isupper():
                    paths.append(current + [neighbor])
                elif neighbor not in current:
                    paths.append(current + [neighbor])
        print(result)

def solution_part2():
    with open('inputs/day12.txt', 'r') as f:
        graph = {}
        for line in f:
            [origin, destination] = line[:-1].split('-')
            if origin not in graph:
                graph[origin] = []
            if destination not in graph:
                graph[destination] = []
            graph[origin].append(destination)
            graph[destination].append(origin)

        result = 0
        paths = [(['start'], None)]
        while len(paths) > 0:
            [current, twice] = paths.pop(0)
            for neighbor in graph[current[-1]]:
                if neighbor == 'end':
                    result += 1
                elif neighbor.isupper():
                    paths.append((current + [neighbor], twice))
                elif neighbor != 'start':
                    if neighbor not in current:
                        paths.append((current + [neighbor], twice))
                    elif twice is None:
                        paths.append((current + [neighbor], neighbor))
        print(result)

solution_part2()
