n = int(input());
arr = [];

for i in range(n):
	val = int(input().split(' ')[0]);
	arr.append(val);

count = [0]*100
for i in arr:
    count[i] += 1;

curr_total = 0;
for val in count:
	curr_total += val;
	print(str(curr_total) + ' ', end = '');
