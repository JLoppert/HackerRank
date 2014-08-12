import math;

jars, ops = input().split(' ');
total = 0;

for i in range(int(ops)):
    start, end, amt = input().split(' ');
    total += ((int(end) - int(start)) + 1) * int(amt);

print(math.floor(total/int(jars)));