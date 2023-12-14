# file_path = "/home/ruan/projects/PractiseProblems/advent_2023/day13-small.txt"
file_path = "/home/ruan/projects/PractiseProblems/advent_2023/day13.txt"

total = 0


def check_vertical_reflection(block):
    row_size = len(block[0])

    for ii in range(len(block[0]) - 1):
        x = ii + 1

        smudges = 0
        for row in block:
            left = x
            right = row_size - x

            if left >= right:
                compare_row = row[::-1]
                compare_row = compare_row[: right * 2]

                mirror = row[::-1]
                mirror = mirror[:right] + mirror[:right][::-1]
            else:
                compare_row = row[: left * 2]
                mirror = row[:left] + row[:left][::-1]

            for ii, elem in enumerate(compare_row):
                if elem != mirror[ii]:
                    smudges += 1

            if smudges > 1:
                break

        if smudges == 1:
            return x

    return None


def check_horizontal_reflection(block):
    transposed_matrix = [list(row) for row in zip(*block)]
    return check_vertical_reflection(transposed_matrix)


def add_value(block):
    v = check_vertical_reflection(block)
    if v:
        return v
    else:
        h = check_horizontal_reflection(block)
        if h:
            return h * 100
    raise AssertionError


total = 0
with open(file_path, "r") as file:
    block = []
    for line in file:
        ll = line.strip()
        if ll:
            block.append(ll)
        else:
            total += add_value(block)
            block = []

    total += add_value(block)

print(total)
