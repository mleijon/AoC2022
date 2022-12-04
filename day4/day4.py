count_a = 0
count_b = 0
count_all = 0
if __name__ == '__main__':
    with open('day4/day4_inp.txt', 'r') as f:
        for line in [x.strip() for x in f.readlines()]:
            count_all += 1
            pair_1 = [int(x) for x in line.split(',')[0].split('-')]
            pair_2 = [int(x) for x in line.split(',')[1].split('-')]
            if (max(pair_1) == max(pair_2)) or (min(pair_1) == min(pair_2)):
                count_a += 1
                continue
            if (max(pair_1) == max(pair_1 + pair_2)) and (min(pair_1) == min(pair_1 + pair_2)):
                count_a += 1
                continue
            if (max(pair_2) == max(pair_1 + pair_2)) and (min(pair_2) == min(pair_1 + pair_2)):
                count_a += 1
                continue
            if (min(pair_1) > max(pair_2)) or (min(pair_2) > max(pair_1)):
                count_b += 1
    print('The answer to part 1 is: {}'.format(count_a))
    print('The answer to part 2 is: {}'.format(count_all - count_b))


