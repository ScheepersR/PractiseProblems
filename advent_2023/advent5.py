file_path = "/home/ruan/projects/advent/day5.txt"


def break_up_ranges(seeds_range, range_2):
    start1, end1 = seeds_range
    start2, end2 = range_2

    if end1 < start2 or end2 < start1:
        return [seeds_range]
    else:
        mid_start = max(start1, start2)
        mid_end = min(end1, end2)

        ranges = [(mid_start, mid_end)]

        if start1 < mid_start:
            ranges.append((start1, mid_start - 1))

        if end1 > mid_end:
            ranges.append((mid_end + 1, end1))

        return ranges


with open(file_path, "r") as file:
    # Iterate through each line in the file

    mapped_to = []
    mapped_split = []
    next_mapped = []

    for line in file:
        line = line.strip()

        if "seeds:" in line:
            seeds = [int(ii) for ii in line.split(": ")[1].split(" ")]

            for ss, rr in zip(seeds[::2], seeds[1::2]):
                mapped_to.append((ss, ss + rr - 1))

        elif line and "map" not in line:
            dest, source, length = [int(ii) for ii in line.split(" ")]

            mapping_range = (source, source + length - 1)

            mapped_split = []
            for s in mapped_to:
                mapped_split = mapped_split + break_up_ranges(s, mapping_range)

            mapped_to = mapped_split

            for s in mapped_to.copy():
                if s[0] >= mapping_range[0] and s[1] <= mapping_range[1]:
                    next_mapped.append((dest + (s[0] - source), dest + (s[1] - source)))
                    mapped_to.remove(s)
        elif not line:
            # empty line, done
            mapped_to = next_mapped + mapped_to
            next_mapped = []
            print(mapped_to)

    mapped_to = next_mapped + mapped_to
    next_mapped = []
    print(mapped_to)

    print(min(mapped_to)[0])
