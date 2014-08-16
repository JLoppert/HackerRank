n = int(input());
arr = [int(i) for i in input().split(' ')];    

p = arr[0];
low = [];
high = [];
for i in range(1, n):
    if p < arr[i]:
        high.append(arr[i]);
    else:
        low.append(arr[i]);
        
low.append(p);
low.extend(high);
print(' '.join(map(str, low)));