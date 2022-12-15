from aocutils.clients.client import fetch, submit

fetch(year=2022, day=9)
moves = list()


def move_tail(position, diff):
    if diff == (2, 0):
        return tuple(map(sum, zip(position, (1, 0))))
    elif diff == (0, 2):
        return tuple(map(sum, zip(position, (0, 1))))
    elif diff == (-2, 0):
        return tuple(map(sum, zip(position, (-1, 0))))
    elif diff == (0, -2):
        return tuple(map(sum, zip(position, (0, -1))))
    elif diff in [(2, 1), (1, 2), (2, 2)]:
        return tuple(map(sum, zip(position, (1, 1))))
    elif diff in [(-2, 1), (-1, 2), (-2, 2)]:
        return tuple(map(sum, zip(position, (-1, 1))))
    elif diff in [(-2, -1), (-1, -2), (-2, -2)]:
        return tuple(map(sum, zip(position, (-1, -1))))
    elif diff in [(1, -2), (2, -1), (2, -2)]:
        return tuple(map(sum, zip(position, (1, -1))))
    else:
        return position


def move_head(position, direction):
    if direction == 'R':
        return tuple(map(sum, zip(position, (1, 0))))
    if direction == 'L':
        return tuple(map(sum, zip(position, (-1, 0))))
    if direction == 'U':
        return tuple(map(sum, zip(position, (0, 1))))
    if direction == 'D':
        return tuple(map(sum, zip(position, (0, -1))))


def calc_rope(knots):
    tail_positions = {(0, 0)}
    positions = list()
    for k in range(knots):
        positions.append((0, 0))
    for move in moves:
        positions[0] = move_head(positions[0], move)
        for k in range(knots - 1):
            diff = tuple(map(lambda i, j: i - j, positions[k], positions[k + 1]))
            positions[k + 1] = move_tail(positions[k + 1], diff)
        tail_positions.add(positions[knots - 1])
    return len(tail_positions)


with open('day9/inputs.txt', 'r') as f:
    for item in [[x.split()[0], int(x.strip().split()[1])] for x in f.readlines()]:
        for _ in range(item[1]):
            moves.append(item[0])

print('The answer to part 1 is: {}'.format(calc_rope(2)))
print('The answer to part 2 is: {}'.format(calc_rope(10)))
submit(calc_rope(2), year=2022, day=9, level=1)
submit(calc_rope(10), year=2022, day=9, level=2)
