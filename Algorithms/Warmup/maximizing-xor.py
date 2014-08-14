# Incomplete Solution

import math;

l = int(input());
r = int(input());

delta = r - l;
ans = 0;
if delta > 0:
    delta_bits = int(math.log2(delta));
    inv = int(math.pow(2, delta_bits)) - 1;
    comp = ~inv;
    upper = r & comp) ^ (l & comp);
    ans = upper + inv;
print(ans);

# Cases:
# 4 4 0 - Pass
# 1 10 15 - Pass
# 5 6 3 - Pass
# 500 544 1023 - Fails