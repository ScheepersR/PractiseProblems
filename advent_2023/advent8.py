# file_path = "/home/ruan/projects/advent/day8-small.txt"
file_path = "/home/ruan/projects/advent/day8.txt"

total = 0

with open(file_path, "r") as file:
    # Iterate through each line in the file
    map = {}
    starts = []
    for line in file:
        # Process each line as needed
        asdf = line.strip()

        if asdf and "=" not in asdf:
            steps = asdf
        elif asdf:
            start, lr = asdf.split(" = ")
            lr = lr.replace("(", "")
            lr = lr.replace(")", "")
            left, right = lr.split(", ")
            map[start] = [left, right]

            if start[-1] == "A":
                starts.append(start)

    moves = 0
    print(starts)

    answers = []

    for ss in starts:
        current = ss
        print(current)
        while current[-1] != "Z":
            index = moves % len(steps)
            m = steps[index]
            current = map[current][m == "R"]
            moves += 1

        answers.append(moves)
        moves = 0

import math

print(math.lcm(*answers))
