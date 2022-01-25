def solution_part1():
    with open("inputs/day20.txt", "r") as f:
        text = f.readlines()
        key = [c for c in text[0][:-1]]
        grid = [[c for c in line[:-1]] for line in text[2:]]

        grid = [["." for _ in range(len(grid[0]) + 4)], ["." for _ in range(len(grid[0]) + 4)]] + \
               [[".", "."] + line + [".", "."] for line in grid] + \
               [["." for _ in range(len(grid[0]) + 4)], ["." for _ in range(len(grid[0]) + 4)]]

        for line in grid:
            print("".join(line))
        print()

        new_grid = [[key[0] for _ in range(len(grid[0]))] for _ in range(len(grid))]

        for row in range(1, len(grid) - 1):
            for col in range(1, len(grid[0]) - 1):
                binary_string = grid[row - 1][col - 1] + grid[row - 1][col] + grid[row - 1][col + 1] + \
                                grid[row][col - 1] + grid[row][col] + grid[row][col + 1] + \
                                grid[row + 1][col - 1] + grid[row + 1][col] + grid[row + 1][col + 1]
                binary_string = "".join(["0" if c == "." else "1" for c in binary_string])
                new_grid[row][col] = key[int(binary_string, 2)]

        for line in new_grid:
            print("".join(line))
        print()

        grid = new_grid

        grid = [[key[0] for _ in range(len(grid[0]) + 2)]] + \
               [[key[0]] + line + [key[0]] for line in grid] + \
               [[key[0] for _ in range(len(grid[0]) + 2)]]


        new_index = 511 if key[0] == "#" else 0

        new_grid = [[key[new_index] for _ in range(len(grid[0]))] for _ in range(len(grid))]

        for row in range(1, len(grid) - 1):
            for col in range(1, len(grid[0]) - 1):
                binary_string = grid[row - 1][col - 1] + grid[row - 1][col] + grid[row - 1][col + 1] + \
                                grid[row][col - 1] + grid[row][col] + grid[row][col + 1] + \
                                grid[row + 1][col - 1] + grid[row + 1][col] + grid[row + 1][col + 1]
                binary_string = "".join(["0" if c == "." else "1" for c in binary_string])
                new_grid[row][col] = key[int(binary_string, 2)]

        for line in new_grid:
            print("".join(line))
        print()

        grid = new_grid

        print(f"Sum:  {sum([line.count('#') for line in grid]) }")


def solution_part2():
    with open("inputs/day20.txt", "r") as f:
        text = f.readlines()
        key = [c for c in text[0][:-1]]
        grid = [[c for c in line[:-1]] for line in text[2:]]

        grid = [["." for _ in range(len(grid[0]) + 4)], ["." for _ in range(len(grid[0]) + 4)]] + \
               [[".", "."] + line + [".", "."] for line in grid] + \
               [["." for _ in range(len(grid[0]) + 4)], ["." for _ in range(len(grid[0]) + 4)]]

        for line in grid:
            print("".join(line))
        print()

        for _ in range(50):
            new_index = 511 if grid[0][0] == "#" else 0
            new_grid = [[key[new_index] for _ in range(len(grid[0]))] for _ in range(len(grid))]

            for row in range(1, len(grid) - 1):
                for col in range(1, len(grid[0]) - 1):
                    binary_string = grid[row - 1][col - 1] + grid[row - 1][col] + grid[row - 1][col + 1] + \
                                    grid[row][col - 1] + grid[row][col] + grid[row][col + 1] + \
                                    grid[row + 1][col - 1] + grid[row + 1][col] + grid[row + 1][col + 1]
                    binary_string = "".join(["0" if c == "." else "1" for c in binary_string])
                    new_grid[row][col] = key[int(binary_string, 2)]

            for line in new_grid:
                print("".join(line))
            print()

            grid = new_grid

            grid = [[key[new_index] for _ in range(len(grid[0]) + 2)]] + \
                   [[key[new_index]] + line + [key[new_index]] for line in grid] + \
                   [[key[new_index] for _ in range(len(grid[0]) + 2)]]

        print(f"Sum:  {sum([line.count('#') for line in grid]) }")



solution_part2()
