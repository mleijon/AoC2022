from aocutils.clients.client import fetch, submit


def find_pack(message, start):
    for i in range(len(message)):
        if len(set(list(stream[i:i + start]))) == start:
            break
    return i + start


if __name__ == '__main__':
    with open('day6/inputs.txt', 'r') as f:
        stream = f.read().strip()

print('The answer to part 1 is: {}'.format(find_pack(stream, 4)))
print('The answer to part 2 is: {}'.format(find_pack(stream, 14)))
submit(find_pack(stream, 4), year=2022, day=6, level=1)
submit(find_pack(stream, 14), year=2022, day=6, level=2)
