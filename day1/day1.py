if __name__ == '__main__':

    with open('day1/day1_inp.txt', 'r') as f:
        cal = 0
        cal_1st = 0
        cal_2nd = 0
        cal_3rd = 0
        for line in f:
            if line.strip().isnumeric():
                cal += int(line.strip())
            else:
                if cal > cal_1st:
                    cal_2nd = cal_1st
                    cal_1st = cal
                    cal = 0
                    continue
                elif cal > cal_2nd:
                    cal_3rd = cal_2nd
                    cal_2nd = cal
                    cal = 0
                    continue
                elif cal > cal_3rd:
                    cal_3rd = cal
                cal = 0
    print('The answer to part 1 is: {}'.format(cal_1st))
    cal_sum = cal_1st + cal_2nd + cal_3rd
    print('The answer to part 2 is: {}'.format(cal_sum))
