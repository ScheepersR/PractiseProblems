# file_path = "/home/ruan/projects/PractiseProblems/advent_2023/day14-small.txt"
file_path = "/home/ruan/projects/PractiseProblems/advent_2023/day14.txt"


def shift_block(block):
    shifted_block = []
    for row in block:
        shifted_row = []
        current_section = [0, 0]
        for rr in row:
            if rr == "#":
                rocks = current_section[1]
                empties = current_section[0]
                shifted_row = shifted_row + ["O"] * rocks + ["."] * empties + ["#"]
                current_section = [0, 0]
            elif rr == "O":
                current_section[1] += 1
            else:
                current_section[0] += 1

        rocks = current_section[1]
        empties = current_section[0]
        shifted_row = shifted_row + ["O"] * rocks + ["."] * empties
        shifted_block.append(shifted_row)

    return shifted_block


def rotate_matrix(matrix):
    matrix = [list(row[::-1]) for row in matrix]
    matrix = list(zip(*matrix))
    return matrix


def run_cycle(block):
    for ii in range(4):
        block = shift_block(block)
        block = rotate_matrix(block)
    return block


total = 0

seen_states = {}

with open(file_path, "r") as file:
    block = [line.strip() for line in file]
    for row in block:
        print(row)

    block = list(zip(*block))
    block = run_cycle(block)

    cycles = 1
    block_hash = hash(str(block))
    while block_hash not in seen_states:
        seen_states[block_hash] = cycles
        block = run_cycle(block)
        block_hash = hash(str(block))
        cycles += 1

    first_seen = seen_states[block_hash]
    second_seen = cycles

    print(first_seen, second_seen)

    all_cycles = 1000000000
    cycle_len = second_seen - first_seen

    extra = ((all_cycles % cycle_len) - first_seen) % cycle_len

    print(extra)
    for x in range(extra):
        block = run_cycle(block)

    total = 0
    distance = len(block)
    for ii, row in enumerate(list(zip(*block))):
        total += (distance - ii) * row.count("O")

    print(total)
