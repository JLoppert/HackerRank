s = int(input());
arr = [int(i) for i in input().split(' ')];
key = arr[-1];

i = 0;
while i < len(arr)-1 and key < arr[-2-i]:
    arr[-1-i] = arr[-2-i];
    i += 1;
    print(' '.join(map(str, arr)));

arr[-1-i] = key;
print(' '.join(map(str, arr)));
