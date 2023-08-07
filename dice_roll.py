from random import randint

found = 0
trials = 100000
for x in range(trials):
    rolls = set([randint(1, 6) for _ in range(6)])
    rolls |= set([randint(1, 6) for _ in range(6 - len(rolls))])

    if len(rolls) == 6:
        found += 1

print(found / trials)
