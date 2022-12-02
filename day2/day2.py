def result(game):
    if game in ['A X', 'B Y', 'C Z']:
        score = 3
    elif game in ['A Y', 'B Z', 'C X']:
        score = 6
    else:
        score = 0
    return [score, game.split()[1]]


def value(choice):
    if choice == 'X':
        return 1
    elif choice == 'Y':
        return 2
    else:
        return 3


def substitute(game):
    if game == 'A X':
        return 'A Z'
    if game == 'B X':
        return 'B X'
    if game == 'C X':
        return 'C Y'
    if game == 'A Y':
        return 'A X'
    if game == 'B Y':
        return 'B Y'
    if game == 'C Y':
        return 'C Z'
    if game == 'A Z':
        return 'A Y'
    if game == 'B Z':
        return 'B Z'
    if game == 'C Z':
        return 'C X'


score_sum_a = 0
score_sum_b = 0
if __name__ == '__main__':
    with open('day2/day2_inp.txt', 'r') as f:
        for line in [x.strip() for x in f.readlines()]:
            score_sum_a += result(line)[0] + value(result(line)[1])
            line = substitute(line)
            score_sum_b += result(line)[0] + value(result(line)[1])

print('The answer to part 1 is: {}'.format(score_sum_a))
print('The answer to part 2 is: {}'.format(score_sum_b))
