import math;

cases = int(input());

for i in range(cases):
    cuts = int(input());
    print(math.floor(cuts/2) * math.ceil(cuts/2));