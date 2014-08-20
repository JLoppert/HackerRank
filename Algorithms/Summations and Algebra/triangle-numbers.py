# http://www.rowan.edu/colleges/csm/departments/math/facultystaff/osler/Variations_on_Pascals_Triangle.pdf
# http://en.wikipedia.org/wiki/Binomial_coefficient
# http://en.wikipedia.org/wiki/Trinomial_expansion
# http://en.wikipedia.org/wiki/Multinomial_theorem

def factorial(val):
    ans = 1;
    while val > 0:
        ans *= val;
        val -= 1;

    return ans;

cases = int(input());
for i in range(cases):
    n = int(input());
    nfact = factorial(n);
    kfact = 1;
    terms = ((n + 2) * (n + 1)) // 2;
    for k in range(terms):
        kfact *= k;
        print(nfact // (kfact * factorial(n-k));