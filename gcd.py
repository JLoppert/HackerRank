# gcd(1071, 462) = 21

# Euclidian Algorithm
def gcd_euclid(a, b):
    while a != b:
        if a > b:
            a -= b;
        else:
            b -= a;
    return a;

def gcd_euclid_rec(a, b):
    if b == 0:
        return a;
    else:
        return (gcd_euclid_rec(b, a % b));