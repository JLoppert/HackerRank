str = input();
map = dict();

for char in str:
    if char in map:
        map[char] += 1;
    else:
        map[char] = 1;

count = list(map.values());
num_odd = sum([val&1 for val in count]);

if num_odd > 1:
    print('NO');
else:
    print('YES')