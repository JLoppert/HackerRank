import math;
cases = int(input());

for case in range(cases):
    stones = int(input());
    a = int(input());
    b = int(input());
    s = set([0]);

    for index in range(stones-1):
        temp = set();

        for elm in range(len(s)):
            curr = s.pop();
            temp.add(curr+a);
            temp.add(curr+b);

        s = temp;

    l = list(s);
    l.sort();
    for elm in l:
        if elm != l[-1]:
            print(str(elm) + ' ', end='');
        else:
            print(elm);