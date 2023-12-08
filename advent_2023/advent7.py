file_path = "/home/ruan/projects/advent/day7.txt"
order = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
total = 0
with open(file_path, "r") as file:
    # Iterate through each line in the file
    hands = [line.strip().split(" ") for line in file]

    def hand_score(hand):
        hand_dist = {}
        num_jokers = 0
        for x in hand:
            if x == "J":
                num_jokers += 1
                continue
            hand_dist.setdefault(x, 0)
            hand_dist[x] += 1

        dist = list(hand_dist.values())
        dist.sort()
        if dist:
            dist[-1] += num_jokers
        else:
            dist = [5]

        if dist == [5]:
            score = tuple([1] + [order.index(card) for card in hand])
        elif dist == [1, 4]:
            score = tuple([2] + [order.index(card) for card in hand])
        elif dist == [2, 3]:
            score = tuple([3] + [order.index(card) for card in hand])
        elif dist == [1, 1, 3]:
            score = tuple([4] + [order.index(card) for card in hand])
        elif dist == [1, 2, 2]:
            score = tuple([5] + [order.index(card) for card in hand])
        elif dist == [1, 1, 1, 2]:
            score = tuple([6] + [order.index(card) for card in hand])
        else:
            score = tuple([7] + [order.index(card) for card in hand])

        # print(hand, dist, score)
        return score

    hands.sort(key=lambda x: hand_score(x[0]), reverse=True)

    total = 0
    for ii, hand in enumerate(hands, start=1):
        total += ii * int(hand[1])

    print(total)
