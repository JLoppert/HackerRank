n = int(input());
arr = [int(i) for i in input().split(' ')];
count = [0]*100
for i in arr:
    count[i] += 1;

print(' '.join(map(str, count)));