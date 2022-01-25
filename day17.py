def solution_part1():
    with open('inputs/day17.txt', 'r') as f:
        arr = [x.split('..') for x in f.readline()[:-1].split('=')]
        arr[1][1] = arr[1][1][:-3]
        x_range = [int(x) for x in arr[1][:2]]
        y_range = [int(y) for y in arr[2]]

        x_step = -1 if x_range[1] < 0 else 1

        max_height = float('-inf')
        launch = None
        for i in range(0, x_range[1] + x_step, x_step):
            for j in range(0, 1000):
                position = [0, 0]
                initial_velocity = [i, j]
                result = fire(position, initial_velocity[:], x_range, y_range, max_height)
                if result[0] and result[1] > max_height:
                    launch = [i, j]
                    max_height = result[1]

        print(launch)
        print(max_height)


def fire(position, velocity, x_range, y_range, max_height):
    while True:
        if position[1] > max_height:
            max_height = position[1]
        if position[0] >= x_range[0] and position[0] <= x_range[1] and \
        position[1] >= y_range[0] and position[1] <= y_range[1]:
            return True, max_height
        elif velocity[0] == 0 and position[0] < x_range[0]:
            return False, max_height
        elif velocity[0] == 0 and position[0] > x_range[1]:
            return False, max_height
        elif velocity[1] <= 0 and position[1] < y_range[0]:
            return False, max_height
        else:
            position[0] += velocity[0]
            position[1] += velocity[1]
            drag = -1 if velocity[0] > 0 else 0 if velocity[0] == 0 else 1
            velocity[0] += drag
            velocity[1] -= 1


def solution_part1():
    with open('inputs/day17.txt', 'r') as f:
        arr = [x.split('..') for x in f.readline()[:-1].split('=')]
        arr[1][1] = arr[1][1][:-3]
        x_range = [int(x) for x in arr[1][:2]]
        y_range = [int(y) for y in arr[2]]

        x_step = -1 if x_range[1] < 0 else 1

        counter = 0
        for i in range(0, x_range[1] + x_step, x_step):
            for j in range(-1000, 1000):
                position = [0, 0]
                initial_velocity = [i, j]
                if fire2(position, initial_velocity[:], x_range, y_range):
                    counter += 1

        print(counter)



def fire2(position, velocity, x_range, y_range):
    while True:
        if position[0] >= x_range[0] and position[0] <= x_range[1] and \
        position[1] >= y_range[0] and position[1] <= y_range[1]:
            return True
        elif velocity[0] == 0 and position[0] < x_range[0]:
            return False
        elif velocity[0] == 0 and position[0] > x_range[1]:
            return False
        elif velocity[1] <= 0 and position[1] < y_range[0]:
            return False
        else:
            position[0] += velocity[0]
            position[1] += velocity[1]
            drag = -1 if velocity[0] > 0 else 0 if velocity[0] == 0 else 1
            velocity[0] += drag
            velocity[1] -= 1

solution_part1()
