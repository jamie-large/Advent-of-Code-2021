import json

class Node:
    def __init__(self, left, right, parent):
        self.left = left
        self.right = right
        self.parent = parent

def parse_number(number, parent=None):
    result = Node(None, None, parent)
    result.left = number[0] if type(number[0]) == int else parse_number(number[0], result)
    result.right = number[1] if type(number[1]) == int else parse_number(number[1], result)
    return result

def recursive_print(number, depth=0):
    print(f"{depth}: {number} with parent {number.parent}")
    if type(number.left) == int:
        print(f"{depth}: {' ' * 3 * (depth-1)}left: {number.left}")
    else:
        recursive_print(number.left, depth + 1)

    if type(number.right) == int:
        print(f"{depth}: {' ' * 3 * (depth-1)}right: {number.right}")
    else:
        recursive_print(number.right, depth + 1)

# def is_reduced(number, depth=0):
#     if depth == 4 or \
#        (type(number.left) == int and number.left >= 10) or \
#        (type(number.right) == int and number.right >= 10):
#         return False

#     left_reduced = True if type(number.left) == int else is_reduced(number.left, depth + 1)
#     right_reduced = True if type(number.right) == int else is_reduced(number.right, depth + 1)

#     return left_reduced and right_reduced

def reduce_explode(number, depth=0):
    if type(number) == int:
        return True
    if depth >= 4 and type(number.left) == int and type(number.right) == int:
        explode(number)
        return False
    # print(f"Reducing node with left {number.left} and right {number.right}")
    return reduce_explode(number.left, depth + 1) and reduce_explode(number.right, depth + 1)

def explode(number):
    # print(f"Exploding node with left {number.left} and right {number.right}")
    movedleft = False
    previous = number
    current = number.parent
    while not movedleft and current != None:
        # print(f"Going left to node with left {current.left} and right {current.right}")
        if current.left == previous:
            previous = current
            current = current.parent
        else:
            movedleft = True
            if type(current.left) == int:
                # print(f"Found destination {current.left}!")
                current.left += number.left
                break
            previous = current
            current = current.left
        while movedleft and type(current.right) != int:
            # print(f"Going left to node with left {current.left} and right {current.right}")
            current = current.right
        if movedleft and type(current.right) == int:
            # print(f"Found destination {current.right}!")
            current.right += number.left

    movedright = False
    previous = number
    current = number.parent
    while not movedright and current != None:
        # print(f"Going right to node with left {current.left} and right {current.right}")
        if current.right == previous:
            previous = current
            current = current.parent
        else:
            movedright = True
            if type(current.right) == int:
                # print(f"Found destination {current.right}!")
                current.right += number.right
                break
            previous = current
            current = current.right
        while movedright and type(current.left) != int:
            # print(f"Going right to node with left {current.left} and right {current.right}")
            current = current.left
        if movedright and type(current.left) == int:
            # print(f"Found destination {current.left}!")
            current.left += number.right

    if number.parent.left == number:
        number.parent.left = 0
    else:
        number.parent.right = 0

def reduce_split(number):
    if type(number) == int:
        return True
    if type(number.left) == int and number.left >= 10:
        split(number)
        return False
    if not reduce_split(number.left):
        return False
    if type(number.right) == int and number.right >= 10:
        split(number)
        return False
    return reduce_split(number.right)


def split(number):
    value = number.left if type(number.left) == int and number.left >= 10 else number.right
    carry = 1 if value % 2 == 1 else 0
    new_number = Node(int(value / 2), int(value / 2) + carry, number)
    if type(number.left) == int and number.left >= 10:
        number.left = new_number
    else:
        number.right = new_number

def reduce(number):
    return reduce_explode(number) and reduce_split(number)

def magnitude(number):
    if type(number) == int:
        return number
    return 3 * magnitude(number.left) + 2 * magnitude(number.right)

def solution_part1():
    with open('inputs/day18.txt', 'r') as f:
        sum = None
        for line in f:
            list_number = json.loads(line[:-1])
            # print(list_number)
            number = parse_number(list_number)

            if sum is None:
                sum = number
                continue

            sum = Node(sum, number, None)
            sum.left.parent = sum
            sum.right.parent = sum

            # recursive_print(sum)
            # print("reducing")
            # reduces = 1
            while not reduce(sum):
                # print(f"After reduce {reduces}")
                # recursive_print(sum)
                # reduces += 1
                pass

        recursive_print(sum)
        print(f"Magnitude {magnitude(sum)}")

def solution_part2():
    with open('inputs/day18.txt', 'r') as f:
        lines = [json.loads(line[:-1]) for line in f.readlines()]
        max_magnitude = float('-inf')

        for i in range(len(lines)):
            for j in range(i, len(lines)):
                sum = Node(parse_number(lines[i]), parse_number(lines[j]), None)
                sum.left.parent = sum
                sum.right.parent = sum
                while not reduce(sum):
                    pass
                mag = magnitude(sum)
                if mag > max_magnitude:
                    max_magnitude = int(mag)

        for i in range(len(lines) - 1, -1, -1):
            for j in range(i, -1, -1):
                sum = Node(parse_number(lines[i]), parse_number(lines[j]), None)
                sum.left.parent = sum
                sum.right.parent = sum
                while not reduce(sum):
                    pass
                mag = magnitude(sum)
                if mag > max_magnitude:
                    max_magnitude = int(mag)

        print(max_magnitude)



solution_part2()
