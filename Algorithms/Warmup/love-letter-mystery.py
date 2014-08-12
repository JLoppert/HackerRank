cases = int(input());

for i in range(cases):
    str = input();
    start = 0;
    end = len(str)-1;
    ans = 0;

    while(start < end):
        ans += abs(ord(str[start]) - ord(str[end]));
        start += 1;
        end -= 1;

    print(ans);