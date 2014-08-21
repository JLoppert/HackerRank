# http://www.rowan.edu/colleges/csm/departments/math/facultystaff/osler/Variations_on_Pascals_Triangle.pdf
# http://en.wikipedia.org/wiki/Binomial_coefficient
# http://en.wikipedia.org/wiki/Trinomial_expansion
# http://en.wikipedia.org/wiki/Multinomial_theorem

cases = int(input());
for case in range(cases):
    n = int(input());
    ans = [3,2,4,2];
    if n < 3:
        print(-1);
    else:
        print(ans[n & 3]);