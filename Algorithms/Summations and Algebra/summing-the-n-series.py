# http://en.wikipedia.org/wiki/Telescoping_series
# sum n**2 - (n-1)**2
# = sum n**2 - (n**2 -2n +1)
# = sum 2n - 1
# = sum 2n - sum 1
# = 2 sum n - sum 1
# = 2 * n(n+1)/2 - n
# = n(n+1) - n
# = n**2 + n - n
# = n**2

cases = int(input());
for i in range(cases):
    n = int(input());
    print(n**2 % ((10**9)+7));