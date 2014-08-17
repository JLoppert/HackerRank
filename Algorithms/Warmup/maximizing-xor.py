import math;

def maxXOR(l, r):
    if l == 0 and r == 0:
        return 0;

    lbit = int(math.log2(l)) if l != 0 else 0;
    rbit = int(math.log2(r)) if r != 0 else 0;

    if lbit != rbit:
        return int(math.pow(2, rbit+1)) - 1;
    else:
        sig_val = int(math.pow(2, rbit));
        return maxXOR(l ^ sig_val, r ^ sig_val);

print(maxXOR(int(input()), int(input())));

# Cases:
# 4 4 0 - Pass
# 1 10 15 - Pass
# 5 6 3 - Pass
# 500 544 1023 - Pass
# 751 982 511 - Pass
# 786 900 255 - Pass
# 304 313 15 - Pass