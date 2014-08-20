def gcd(a, b):
    if b == 0:
        return a;
    else:
        return (gcd(b, a % b));

cases = int(input());
for i in range(cases):
    size = int(input());
    arr = [int(i) for i in input().split()];
    gc = 0;
    for val in arr:
        gc = gcd(val, gc);

    if gc == 1:
        print('YES');
    else:
        print('NO');