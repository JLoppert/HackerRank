T = int(input());
for i in range(T):
    N, K = [int(j) for j in input().split(' ')];
    A = [int(j) for j in input().split(' ')];
    B = [int(j) for j in input().split(' ')];

    A.extend(B);
    A.sort();
    found = True;
    for i in range(N):
        if A[i] + A[-1-i] < K:
            found = False;
            break;

    if found:
        print('YES');
    else:
        print('NO');