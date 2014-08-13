n = int(input());
m = [0]*n;
ans = [0]*n;

for i in range(n):
    line = input();
    m[i] = [int(i) for i in line];
    ans[i] = [int(i) for i in line];

if n > 2:
    for row in range(1, n-1):
        for col in range(1, n-1):
            l = [];
            cur = m[row][col];
            top = m[row-1][col];
            bottom = m[row+1][col];
            left = m[row][col-1];
            right = m[row][col+1];
            if top < cur and bottom < cur and left < cur and right < cur:
                ans[row][col] = 'X';

for i in ans:
    print(''.join(map(str, i)));