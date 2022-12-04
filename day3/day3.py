import string

priorities = list(string.ascii_lowercase) + list(string.ascii_uppercase)

sum_priorities_a = 0
sum_priorities_b = 0
counter = 0
group = ['']*3
if __name__ == '__main__':
    with open('day3/day3_inp.txt', 'r') as f:
        for line in [x.strip() for x in f.readlines()]:
            item = set(line[:len(line)//2]).intersection(set(line[len(line)//2:]))
            sum_priorities_a += priorities.index((list(item)[0])) + 1
            if counter == 2:
                group[counter] = line
                item2 = set(group[0]).intersection(set(group[1])).intersection(set(group[2]))
                sum_priorities_b += priorities.index((list(item2)[0])) + 1
                counter = 0
            else:
                group[counter] = line
                counter += 1
print('The answer to part 1 is: {}'.format(sum_priorities_a))
print('The answer to part 2 is: {}'.format(sum_priorities_b))
