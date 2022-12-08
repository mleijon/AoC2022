# from aocutils.clients.client import fetch, submit
from collections import defaultdict
# fetch(year=2022, day=7)


current_dir = '/'
dir_sizes = dict()
dir_sizes['/'] = 'start'
dir_sizes_tot = defaultdict(lambda: 0)
size = 0
if __name__ == '__main__':
    with open('day7/test', 'r') as f:
        for line in f:
            print(current_dir)
            if line.startswith('$ cd '):
                dir_sizes[current_dir] = size
                change_dir = ''.join(line.strip().split()[-1:])
                if change_dir == '/':
                    current_dir = '/'
                    continue
                elif change_dir == '..':
                    current_dir = current_dir.rsplit('/', 2)[0] + '/'
                    continue
                else:
                    current_dir += change_dir + '/'
                    continue
            elif line.startswith('$ ls'):
                size = 0
                continue
            elif line.startswith('dir'):
                continue
            else:
                size += int(line.split()[0])

    # for item1 in dir_sizes:
    #     for item2 in dir_sizes:
    #         if item2.startswith(item1):
    #             dir_sizes_tot[item1] += dir_sizes[item2]

    print(dir_sizes)



# submit(, year=2022, day=7, level=1)
# submit(, year=2022, day=7, level=2)