file_path = "/home/ruan/projects/advent/day4.txt"

total = 0
with open(file_path, "r") as file:
    copies = [1 for _ in range(209)]
    for ii, line in enumerate(file):
        game = line.strip()
        remove_game_num = game.split(": ")[1]

        winners, numbers = remove_game_num.split(" | ")

        winners = list(filter(bool, winners.split(" ")))
        numbers = list(filter(bool, numbers.split(" ")))

        total_wins = len([x for x in numbers if x in winners])

        for x in range(total_wins):
            copies[ii + 1 + x] += copies[ii]


print(sum(copies))
