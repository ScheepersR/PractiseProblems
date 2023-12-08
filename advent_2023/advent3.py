import numpy as np

file_path = "/home/ruan/projects/advent/day3.txt"

SIZE_OF_GRID = 140

gears = {}


def run():
    total = 0
    with open(file_path, "r") as file:
        # Iterate through each line in the file
        lines = [line.strip() for line in file]

    for rowi, line in enumerate(lines):
        parsing_num = ""
        num = None

        for chari, char in enumerate(line):
            if char.isnumeric():
                parsing_num += char

            if (parsing_num and not char.isnumeric()) or (
                parsing_num and chari == SIZE_OF_GRID - 1
            ):
                num = int(parsing_num)
                parsing_num = ""

                if (chari == SIZE_OF_GRID - 1) and char.isnumeric():
                    x_index = chari
                else:
                    x_index = chari - 1

                # if is_part(lines, rowi, x_index, num):
                #     print(num)
                #     total += num
                #     num = None

                check_gear(lines, rowi, x_index, num)

    for gear_ratio in gears.values():
        if len(gear_ratio) == 2:
            total += gear_ratio[0] * gear_ratio[1]

    print(total)


def is_part(lines, rowi, chari, num):
    adj_points = set()
    for x in range(len(str(num))):
        adj_points.update(get_adjacent_points(chari - x, rowi))

    for x, y in adj_points:
        adj_char = lines[y][x]
        if adj_char != "." and not adj_char.isnumeric():
            return True

    return False


def check_gear(lines, rowi, chari, num):
    adj_points = set()
    for x in range(len(str(num))):
        adj_points.update(get_adjacent_points(chari - x, rowi))

    for x, y in adj_points:
        adj_char = lines[y][x]
        if adj_char == "*":
            gears.setdefault((y, x), []).append(num)

    return False


def get_adjacent_points(x, y):
    points = set()
    for ii in range(9):
        values = np.base_repr(ii, base=3).zfill(2)
        ax = x + [-1, 0, 1][int(values[0])]
        ay = y + [-1, 0, 1][int(values[1])]

        if ax >= 0 and ax < SIZE_OF_GRID and ay >= 0 and ay < SIZE_OF_GRID:
            points.add((ax, ay))

    return points


run()
