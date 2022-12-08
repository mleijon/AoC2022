# from aocutils.clients.client import fetch, submit

# fetch(year=2022, day=7)
def sum_size():
    pass
current_dir = ''
dir_sizes = dict()
if __name__ == '__main__':
    with open('day7/inputs.txt', 'r') as f:
        for line in f:
            if line.startswith('$ cd '):
                change_dir = ''.join(line.strip().split()[-1:])
                if change_dir == '/':
                    current_dir += '/'
                    dir_sizes[current_dir] = sum_size(current_dir)
                    continue
                elif change_dir == '..':
                    current_dir = current_dir.rsplit('/', 1)[0]
                else:
                    current_dir += '/' + change_dir


# submit(, year=2022, day=7, level=1)
# submit(, year=2022, day=7, level=2)
