T = int(input());

for i in range(T):
    N = int(input());
    arr = [int(i) for i in input().split(' ')];
    
    left = 0;
    right = sum(arr) - arr[0];
    found = False;
    for i in range(N):
        if left == right:
            found = True;
            break;
        else:
            left += arr[i];
            right -= arr[i+1] if i+1 < N else 0;
            
    if found:
        print('YES');
    else:
        print('NO');