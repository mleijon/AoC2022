from aocutils.clients.client import fetch, submit

fetch(year=2022, day=8)


def is_visible(row, col):
    vis_top = True
    vis_bot = True
    vis_lft = True
    vis_rgt = True
    view = 1
    tree = forest[row][col]
    for r in range(row - 1, -1, -1):
        if forest[r][col] >= tree:
            vis_top = False
            view *= row - r
            break
        elif r == 0:
            view *= row
    for r in range(row + 1, max_row):
        if forest[r][col] >= tree:
            vis_bot = False
            view *= r - row
            break
        elif r == max_row - 1:
            view *= max_row - (row + 1)
    for c in range(col - 1, -1, -1):
        if forest[row][c] >= tree:
            vis_lft = False
            view *= col - c
            break
        elif c == 0:
            view *= col
    for c in range(col + 1, max_col):
        if forest[row][c] >= tree:
            vis_rgt = False
            view *= c - col
            break
        elif c == max_col - 1:
            view *= max_col - (col + 1)
    return vis_top or vis_bot or vis_rgt or vis_lft, view


forest = list()
with open('day8/inputs.txt', 'r') as f:
    for row in f:
        forest.append([int(x) for x in list(row.strip())])
max_row = len(forest[0])
max_col = len(forest)
visible = 2 * max_row + 2 * (max_col - 2)
view_max = 0
for row in range(1, max_row - 1):
    for col in range(1, max_col - 1):
        visible += is_visible(row, col)[0]
        view_max = max(view_max, is_visible(row, col)[1])
print('The answer to part 1 is: {}'.format(visible))
print('The answer to part 2 is: {}'.format(view_max))
submit(visible, year=2022, day=8, level=1)
submit(view_max, year=2022, day=8, level=2)
