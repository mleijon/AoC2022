from aocutils.clients.client import fetch, submit
import copy

fetch()
crates = list()
pile = list()
if __name__ == '__main__':
    with open('day5/inputs.txt', 'r') as f:
        crates_rev, moves = f.read().split('\n\n')
    crates_rev = crates_rev.split('\n')
    nr_of_piles = int(crates_rev.pop().split().pop())
    levels_start = len(crates_rev)
    for i in range(levels_start):
        crates_rev[i] = [crates_rev[i][j: j + 4] for j in range(0, len(crates_rev[i]), 4)]
    for i in range(nr_of_piles):
        for j in range(levels_start - 1, -1, -1):
            pile.append(crates_rev[j][i].strip())
        for item in reversed(pile):
            if item == '':
                pile.pop()
        crates.append(pile)
        pile = []
crates_a = copy.deepcopy(crates)
crates_b = copy.deepcopy(crates)
m = [x.split() for x in moves.split('\n')]
moves = []
for item in m:
    moves.append([int(item[1]), int(item[3]), int(item[5])])

pile = []
for m in moves:
    for _ in range(m[0]):
        cratea = crates_a[m[1] - 1].pop()
        crateb = crates_b[m[1] - 1].pop()
        crates_a[m[2] - 1].append(cratea)
        pile.insert(0, crateb)
    crates_b[m[2] - 1] += pile
    pile = []

answer_a = str()
answer_b = str()
for crate in crates_a:
    answer_a += crate[-1:][0][1]
for crate in crates_b:
    answer_b += crate[-1:][0][1]
print('The answer to part 1 is: {}'.format(answer_a))
print('The answer to part 2 is: {}'.format(answer_b))
submit(answer_a, year=2022, day=5, level=1)
submit(answer_b, year=2022, day=5, level=2)
