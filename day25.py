def solution_part1():
    with open("inputs/day25.txt", "r") as f:
        grid = [[c for c in line[:-1]] for line in f.readlines()]

        moved = True
        count = 0
        while moved:
            count += 1
            moved = False
            # Move snails east
            for row in range(len(grid)):
                col = 0
                front_occupied = grid[row][0] != "."
                while col < (len(grid[0]) - 1):
                    if grid[row][col] == ">" and grid[row][col + 1] == ".":
                        grid[row][col + 1] = ">"
                        grid[row][col] = "."
                        col += 1
                        moved = True
                    col += 1
                if col < len(grid[0]) and grid[row][-1] == ">" and not front_occupied:
                    grid[row][0] = ">"
                    grid[row][-1] = "."
                    moved = True

            # Move snails south
            for col in range(len(grid[0])):
                row = 0
                front_occupied = grid[0][col] != "."
                while row < (len(grid) - 1):
                    if grid[row][col] == "v" and grid[row + 1][col] == ".":
                        grid[row + 1][col] = "v"
                        grid[row][col] = "."
                        row += 1
                        moved = True
                    row += 1
                if row < len(grid) and grid[-1][col] == "v" and not front_occupied:
                    grid[0][col] = "v"
                    grid[-1][col] = "."
                    moved = True

        print(count)


solution_part1()
