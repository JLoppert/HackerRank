cases = int(input());
for i in range(cases):
    mystery = int(input());
    fib1 = 0
    fib2 = 1;
    while fib2 < mystery:
        temp = fib2;
        fib2 = fib1+fib2;
        fib1 = temp;

    if fib2 == mystery:
        print('IsFibo');
    else:
        print('IsNotFibo');