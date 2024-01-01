import toolz

file_path = "/home/ruan/Projects/PractiseProblems/advent_2023/day9.txt"

total = 0
with open(file_path, "r") as file:
    for line in file:
        sequence = [int(x) for x in line.strip().split(" ")]

        sequences = [sequence]
        while len(set(sequences[-1])) != 1:
            next_sequence = [y - x for x, y in toolz.sliding_window(2, sequences[-1])]
            sequences.append(next_sequence)

        prev_val = 0
        for seq in reversed(sequences):
            prev_val = seq[0] - prev_val

        total += prev_val

print(total)
