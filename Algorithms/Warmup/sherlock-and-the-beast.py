cases = int(input());
for i in range(cases):
    val = int(input());
    l = [''];
    for index in range(val):
        for elm in range(len(l)):
            curr = l.pop(0);
            l.append(curr + '5');
            l.append(curr + '3');
    
    largest = -1
    for elm in l:
        m = {'3': 0, '5':0};
        ls = list(elm);
        for item in ls:
            m[item] += 1;
        
        if m['3'] % 5 == 0 and m['5'] % 3 == 0 and int(elm) > largest:
            largest = int(elm);
    
    print(largest);