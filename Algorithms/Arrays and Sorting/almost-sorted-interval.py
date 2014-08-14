# Not optimal solution
# Fails and timesout for multiple cases

n = int(input());
arr = [int(i) for i in input().split(' ')];

count = 0;
for i in range(n):
    count += 1;
    j = i+1;
    while j < n and arr[j-1] < arr[j]:
        count += 1;

print(count);