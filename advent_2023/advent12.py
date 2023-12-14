# file_path = "/home/ruan/projects/PractiseProblems/advent_2023/day12-small.txt"
file_path = "/home/ruan/projects/PractiseProblems/advent_2023/day12.txt"

from functools import cache
import time


def count_row(row):
    return tuple([size for ss in row.split(".") if (size := len(ss))])


def create_dot_child(row, counts):
    start, end = row.split("?", 1)

    if not start:
        return (end.lstrip("."), counts)

    start_counts = count_row(start)
    start_index = len(start_counts)
    if start_counts == counts[:start_index]:
        return (end.lstrip("."), counts[start_index:])

    return None


def create_hash_child(row, counts):
    start, end = row.split("?", 1)

    start = start + "#"

    start_counts = count_row(start)
    start_index = len(start_counts)

    if len(start_counts) > len(counts):
        return None

    for ii, cc in enumerate(start_counts[:-1]):
        if cc != counts[ii]:
            return None

    required = counts[start_index - 1] - start_counts[-1]
    remaining_counts = counts[start_index:]

    if required < 0:
        return None
    elif not required:
        if not end.lstrip("."):
            return (end.lstrip("."), remaining_counts)
        elif end[0] == ".":
            return (end.lstrip("."), remaining_counts)
        elif end[0] == "?":
            return (end[1::].lstrip("."), remaining_counts)
    elif required > len(end):
        return None
    else:
        block = end[:required]
        new_end = end[required:]

        if "." in set(block):
            return None
        elif new_end and new_end[0] == "#":
            return None
        elif new_end and new_end[0] == "?":
            return (end[required + 1 :].lstrip("."), remaining_counts)
        else:
            return (new_end.lstrip("."), remaining_counts)


@cache
def dfs(row, counts):
    if not row and not counts:
        return 1
    elif not row and counts:
        return 0

    required = sum(counts)
    current_hashes = row.count("#")
    remaining = row.count("?")

    if current_hashes + remaining == required:
        row = row.replace("?", "#")
        return 1 if count_row(row) == counts else 0

    if current_hashes == required:
        check_row_dot = row.replace("?", ".")
        return 1 if count_row(check_row_dot) == counts else 0

    if current_hashes + remaining < required:
        return 0

    if current_hashes > required:
        return 0

    dot_child = create_dot_child(row, counts)
    hash_child = create_hash_child(row, counts)

    total = 0
    for child_row, child_counts in filter(bool, [dot_child, hash_child]):
        total += dfs(child_row, child_counts)

    return total


start_time = time.time()

total = 0
with open(file_path, "r") as file:
    for line in file:
        sub_total = 0
        row, counts = line.strip().split(" ")
        counts = [int(x.strip()) for x in counts.split(",")]

        row = "?".join([row for _ in range(5)])
        counts = counts * 5
        print(row, counts)

        dfs.cache_clear()
        sub = dfs(row, tuple(counts))
        print(sub)
        total += sub

print(total)
# Record end time
end_time = time.time()

# Calculate and print the elapsed time
print(end_time - start_time)
