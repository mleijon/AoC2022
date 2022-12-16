from aocutils.clients.client import fetch, submit

fetch(year=2022, day=10)

signal = 1
signal_strength = 0
cycle = 0
collect = [20, 60, 100, 140, 180, 220]
with open('day10/inputs.txt', 'r') as f:
    instructions = [tuple(x.strip().split()) for x in f.readlines()]
    for i in instructions:
        if i[0] == 'noop':
            cycle += 1
            if cycle in collect:
                signal_strength += cycle*signal
            if (cycle - 1) % 40 in [signal - 1, signal, signal + 1]:
                print('#', end="")
            else:
                print(".", end="")
        elif i[0] == 'addx':
            cycle += 2
            if cycle - 1 in collect:
                signal_strength += (cycle - 1) * signal

            if (cycle - 2) % 40 in [signal - 1, signal, signal + 1]:
                print('#', end="")
            else:
                print(".", end="")
            if (cycle - 1) % 40 == 0:
                print()
            if cycle in collect:
                signal_strength += cycle*signal
            if (cycle - 1) % 40 in [signal - 1, signal, signal + 1]:
                print('#', end="")
            else:
                print(".", end="")
            signal += int(i[1])
        if cycle % 40 == 0:
            print()
print('The answer to part 1 is: {}'.format(signal_strength))
print('The answer to part 2 is: {}'.format('ZRARLFZU'))
submit(signal_strength, year=2022, day=10, level=1)
submit('ZRARLFZU', year=2022, day=10, level=2)
