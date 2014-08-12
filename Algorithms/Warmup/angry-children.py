bags = int(input());
window = int(input());
l = [];

for i in range(bags):
    l.append(int(input()));

l.sort();
index = 0;
ans = float('inf');
while index + window-1 < bags:
    diff = l[index+window-1] - l[index];
    if diff < ans:
        ans = diff;
    index += 1;

print(ans);