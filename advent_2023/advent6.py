file_path = "/home/ruan/projects/PractiseProblems/advent_2023/day6-small.txt"
# file_path = "/home/ruan/projects/PractiseProblems/advent_2023/day6.txt"

total = 0

times = []
distance = []

from numpy import roots
from math import floor, ceil

solves = []
for ii, t in enumerate(times):
    dist_to_beat = distance[ii]

    soln = roots([-1, t, -(dist_to_beat + 0.01)])

    minn = ceil(min(soln))
    maxx = floor(max(soln))

    solves.append(maxx - minn + 1)

from functools import reduce
from operator import mul

print(solves)
print(reduce(mul, solves))
