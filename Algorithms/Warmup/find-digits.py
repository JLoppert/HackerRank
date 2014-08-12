cases = int(input());

for i in range(cases):
    org = int(input());
    val = org;
    count = 0;
    lookup = [];
    while val  > 0:
        cur = val % 10;
        val = int(val/10);

        if cur == 0:
            continue;

        if cur in lookup:
            count += 1;

        if org % cur == 0 and cur not in lookup:
            lookup.append(cur);
            count += 1;

    print(count);