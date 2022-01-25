def solution_part1():
    num = 9999999 + 1
    while True:
        num -= 1

        [a, b, c, d, f, g, i] = [int(c) for c in str(num)]
        if 0 in (a, b, c, d, f, g, i):
            continue

        z = a
        z = 26*z + b + 12
        z = 26*z + c + 14
        z = 26*z + d
        e = (z % 26) - 2
        if e < 1 or e > 9:
            continue
        z = int(z / 26)
        z = 26*z + f + 15
        z = 26*z + g + 11
        h = (z % 26) - 15
        if h < 1 or h > 9:
            continue
        z = int(z / 26)
        z = 26 * z + i + 1
        j = (z % 26) - 9
        if j < 1 or j > 9:
            continue
        z = int(z / 26)
        k = (z % 26) - 9
        if k < 1 or k > 9:
            continue
        z = int(z / 26)
        l = (z % 26) - 7
        if l < 1 or l > 9:
            continue
        z = int(z / 26)
        m = (z % 26) - 4
        if m < 1 or m > 9:
            continue
        z = int(z / 26)
        n = (z % 26) - 6
        if n < 1 or n > 9:
            continue
        z = int(z / 26)

        if (z == 0):
            print(f"{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}{m}{n}")
            return

def solution_part2():
    num = 999999
    while True:
        num += 1

        [a, b, c, d, f, g, i] = [int(c) for c in str(num)]
        if 0 in (a, b, c, d, f, g, i):
            continue

        z = a
        z = 26*z + b + 12
        z = 26*z + c + 14
        z = 26*z + d
        e = (z % 26) - 2
        if e < 1 or e > 9:
            continue
        z = int(z / 26)
        z = 26*z + f + 15
        z = 26*z + g + 11
        h = (z % 26) - 15
        if h < 1 or h > 9:
            continue
        z = int(z / 26)
        z = 26 * z + i + 1
        j = (z % 26) - 9
        if j < 1 or j > 9:
            continue
        z = int(z / 26)
        k = (z % 26) - 9
        if k < 1 or k > 9:
            continue
        z = int(z / 26)
        l = (z % 26) - 7
        if l < 1 or l > 9:
            continue
        z = int(z / 26)
        m = (z % 26) - 4
        if m < 1 or m > 9:
            continue
        z = int(z / 26)
        n = (z % 26) - 6
        if n < 1 or n > 9:
            continue
        z = int(z / 26)

        if (z == 0):
            print(f"{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}{m}{n}")
            return


solution_part2()
