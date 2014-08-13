n = int(input());
arr = [int(i) for i in input().split(' ')];
count = [0]*100
for i in arr:
    count[i] += 1;

ans = [];
for value, times in zip(range(100), count):
	ans.extend([value]*times);

print(' '.join(map(str, ans)));
