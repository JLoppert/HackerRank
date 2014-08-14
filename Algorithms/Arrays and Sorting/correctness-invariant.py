s = int(input());
arr = [int(i) for i in input().split(' ')];

for i in range(s):
    j = i;
    if j > 0 and arr[j] < arr[j-1]:
        while j-1 >= 0 and arr[j] < arr[j-1]:
            tmp = arr[j-1];
            arr[j-1] = arr[j];
            arr[j] = tmp;
            j -= 1;
print(' '.join(map(str,arr)));