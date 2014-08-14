# Incomplete solution

# Solve: N = (3*x) + (5*y)
# N = length of string
# x = number of 5s
# y = number of 3s
# x = (N - (5*y)) / 3

cases = int(input());
for i in range(cases):
    n = int(input());


    # l = [''];
    # for index in range(val):
    #     for elm in range(len(l)):
    #         curr = l.pop(0);
    #         l.append(curr + '5');
    #         l.append(curr + '3');

    # largest = -1
    # for elm in l:
    #     m = {'3': 0, '5':0};
    #     ls = list(elm);
    #     for item in ls:
    #         m[item] += 1;

    #     if m['3'] % 5 == 0 and m['5'] % 3 == 0 and int(elm) > largest:
    #         largest = int(elm);

    # print(largest);