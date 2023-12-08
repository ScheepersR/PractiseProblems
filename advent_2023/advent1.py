file_path = "/home/ruan/projects/advent/input1.txt"

total = 0
with open(file_path, "r") as file:
    # Iterate through each line in the file
    for line in file:
        # Process each line as needed
        asdf = line.strip()
        first = None
        last = None

        for ii, c in enumerate(asdf):
            try:
                num = int(c)
                first = num if first is None else first
                last = num
            except ValueError:
                for jj, num_s in enumerate(
                    [
                        "one",
                        "two",
                        "three",
                        "four",
                        "five",
                        "six",
                        "seven",
                        "eight",
                        "nine",
                    ],
                    start=1,
                ):
                    if num_s == asdf[ii : ii + len(num_s)]:
                        num = jj
                        first = num if first is None else first
                        last = num
        # print(first, last)
        total = total + first * 10 + last


print(total)
