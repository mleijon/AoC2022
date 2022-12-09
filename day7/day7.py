from aocutils.clients.client import fetch, submit
from collections import defaultdict

fetch(year=2022, day=7)
current_dir = '/'
dir_sizes = dict()
dir_sizes_tot = defaultdict(lambda: 0)
size = -1
if __name__ == '__main__':
    with open('day7/inputs.txt', 'r') as f:
        for line in f:
            if line.strip() == '$ cd /' and (size == - 1):
                continue
            else:
                if line.startswith('$ cd '):
                    dir_sizes[old_dir] = size
                    change_dir = ''.join(line.strip().split()[-1:])
                    if change_dir == '..':
                        current_dir = current_dir.rsplit('/', 2)[0] + '/'
                    else:
                        current_dir += change_dir + '/'
                elif line.startswith('$ ls'):
                    old_dir = current_dir
                    size = 0
                elif line.startswith('dir'):
                    continue
                else:
                    size += int(line.split()[0])
        dir_sizes[current_dir] = size
    for item1 in dir_sizes:
        for item2 in dir_sizes:
            if item2.startswith(item1):
                dir_sizes_tot[item1] += dir_sizes[item2]
    sum_a = 0
    for item in dir_sizes_tot.values():
        if item < 100000:
            sum_a += item

    space_available = 70000000 - dir_sizes_tot['/']
    space_needed = 30000000 - space_available
    current_largest = dir_sizes_tot['/']
    for item in dir_sizes_tot.values():
        if space_needed <= item < current_largest:
            current_largest = item
    print('The answer to part 1 is: {}'.format(sum_a))
    print('The answer to part 2 is: {}'.format(current_largest))
    submit(sum_a, year=2022, day=7, level=1)
    submit(current_largest, year=2022, day=7, level=2)
