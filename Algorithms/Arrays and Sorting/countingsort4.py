n = int(input());
d = dict();
for i in range(n):
    key, value = input().split(' ');
    key = int(key);
    if key not in d:
        d[key] = [];
        
    if i < int(n/2):
        value = '-';

    d[key].append(value);

for i in range(len(d)):
    print(' '.join(d[i]), end = ' ');