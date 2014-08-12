cases = int(input());
set = {i for i in input()};

for i in range(cases-1):
    newSet = {i for i in input()};
    set = set & newSet;

print(len(set));