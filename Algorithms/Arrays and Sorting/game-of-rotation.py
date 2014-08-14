# Optimal Solution
# Ex: [a, b, c, d]
# Init = a + 2b + 3c + 4d
# Rot1 =      b + 2c + 3d + 4a
# Delta = -a -b -c -d + 4a
# Solution - use delta to compute rotation in linear time

n = int(input());
arr = [int(i) for i in input().split(' ')];
s = sum(arr);

total = 0;
for i in range(1, n+1):
    # weighted sum for Rot0
    total += arr[i-1] * i;

ans = total;

for i in range(n):
    # compute next Rot using delta
    total = total - s + (n*arr[i]);
    ans = max(ans, total);

print(ans);