file_path = "/home/ruan/projects/advent/input3.txt"
from functools import reduce
import operator

total = 0
legal = {"red": 12, "green": 13, "blue": 14}
with open(file_path, "r") as file:
    # Iterate through each line in the file

    for game_id, line in enumerate(file, start=1):
        # Process each line as needed
        asdf = line.strip()
        games = asdf.split(":")[1].split(";")
        max_colours = {"blue": 0, "red": 0, "green": 0}
        for game in games:
            for draw in game.split(","):
                value, key = draw.strip().split(" ")
                value = int(value)
                max_colours[key] = max(value, max_colours[key])

        power = reduce(operator.mul, max_colours.values(), 1)
        total += power

print(total)
